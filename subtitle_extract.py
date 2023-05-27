import argparse
from pathlib import Path
import os
import srt
import re
import codecs
import glob
import m3u8
import ffmpeg


def download_video_to_file(uri: str, output: Path):
    ffmpeg.input(uri).output(output, codec="copy").run()


def pull_playlist(args: argparse.Namespace):
    os.makedirs(args.output_folder, exist_ok=True)

    playlists = m3u8.load(args.input_playlist)

    for playlist in playlists.playlists:
        # if there is only 640x360 and 1280x720, it's the screen
        # if there are 3 streams, it's the room
        # the subs are the same
        if (
            playlist.stream_info.resolution[1] == 720
            and playlist.stream_info.bandwidth > 700000
        ):
            download_video_to_file(playlist.uri, f"{args.output_folder}/{args.output_folder}_room.mkv")
        if (
            playlist.stream_info.resolution[1] == 720
            and playlist.stream_info.bandwidth < 800000
        ):
            download_video_to_file(playlist.uri, f"{args.output_folder}/{args.output_folder}_screen.mkv")


def extract_video(args: argparse.Namespace):
    expr = args.expression
    for name in glob.glob("**/*.srt"):
        path = Path(name)
        stem = path.stem
        print(name)

        match_timestamps = []

        with open(name, "rb") as f:
            r_enc = codecs.getreader("utf-8-sig")
            lines = r_enc(f).read()
            subs = list(srt.parse(lines))
            for sub in subs:
                if len(sub.content) > 0 and re.search(expr, sub.content):
                    match_timestamps.append((sub.start.seconds, sub.end.seconds))
        in_file = ffmpeg.input(f"{stem}.mkv")
        streams = [
            in_file.trim(start=start, end=end) for start, end in match_timestamps
        ]
        ffmpeg.concat(*streams).output("out.mp4").run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action", choices=["pull_playlist", "extract_video"]
    )
    parser.add_argument("--output_folder")
    parser.add_argument("--input_playlist")
    parser.add_argument("--expression")
    args = parser.parse_args()
    match args.action:
        case "pull_playlist":
            pull_playlist(args)
        case "extract_video":
            extract_video(args)
        case _:
            raise Exception("Not a valid action")
