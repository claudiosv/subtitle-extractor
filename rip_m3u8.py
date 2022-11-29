import argparse
from pathlib import Path
import os
import time
parser = argparse.ArgumentParser()
parser.add_argument('date')
parser.add_argument('input_playlist')
args = parser.parse_args()
os.makedirs(args.date, exist_ok = True)
import subprocess
from subprocess import Popen
import m3u8
playlists = m3u8.load(args.input_playlist)
playlists.dump(f"{args.date}.m3u8")
print(f"Is variant: {playlists.is_variant}")
num_playlists = len(playlists.playlists)
running_procs = []
for playlist in playlists.playlists:
    # if there is only 640x360 and 1280x720, it's the screen
    # if there are 3 streams, it's the room
    # the subs are the same
    print(playlist.uri)
    print(playlist.stream_info.resolution)
    if playlist.stream_info.resolution[1] == 720 and playlist.stream_info.bandwidth>700000:
        #running_procs.append(Popen(['ffmpeg', '-i', playlist.media[0].uri, f"{args.date}/{args.date}.srt"]))
        running_procs.append(Popen(['ffmpeg', '-i', playlist.uri, '-codec', 'copy', f"{args.date}/{args.date}_room.mkv"]))
    if playlist.stream_info.resolution[1] == 720 and playlist.stream_info.bandwidth<800000:
        running_procs.append(Popen(['ffmpeg', '-i', playlist.uri, '-codec', 'copy', f"{args.date}/{args.date}_screen.mkv"]))
    #print(playlist.media[0].uri)
    
while running_procs:
    for proc in running_procs:
        retcode = proc.poll()
        if retcode is not None: # Process finished.
            running_procs.remove(proc)
            break
        else: # No process is done, wait a bit and check again.
            time.sleep(.1)
            if proc.stdout is not None:
              print(proc.stdout)
            continue
