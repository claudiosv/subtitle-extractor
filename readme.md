# Subtitle Extractor

Subtitle Extractor is a Python script that allows you to download videos from m3u8 playlists and extract segments of video where the subtitles match a regular expression.

```shell
usage: subtitle_extract.py [-h] [--output_folder OUTPUT_FOLDER] [--input_playlist INPUT_PLAYLIST] [--expression EXPRESSION] {pull_playlist,extract_video}

positional arguments:
  {pull_playlist,extract_video}

options:
  -h, --help            show this help message and exit
  --output_folder OUTPUT_FOLDER
  --input_playlist INPUT_PLAYLIST
  --expression EXPRESSION
```

## Features

- Download streams from m3u8 playlist (currently some hard coded assumptions)
- User-friendly command-line interface
- Cross-platform compatibility (Windows, macOS, Linux)

## Installation

1. Clone this repository to your local machine using the following command:

   ```shell
   git clone https://github.com/claudiosv/subtitle-extractor.git
   ```

2. Navigate to the project directory:

   ```shell
   cd subtitle-extractor
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

To download videos from a m3u8 playlist, run the following command:

```shell
python subtitle_extractor.py --output_folder videos --input_playlist http://video_website.com/a-m3u8-playlist
```

Once you have videos, download or find a subtitle file for each in the SRT file format. It assumes that the subtitle file will have the same name as the video, which **must** end in .mkv e.g. myvideo.srt <-> myvideo.mkv. You can then run a command with a regular expression:

```shell
python subtitle_extractor.py --expression "(kinda|sense)"
```

It will then produce a file "out.mp4" of all the segments where the subtitle contained a regex match, concatenated.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue on the [GitHub repository](https://github.com/claudiosv/subtitle-extractor/issues).

If you'd like to contribute code, please fork the repository, create a new branch, make your changes, and submit a pull request. Make sure to follow the existing coding style and include relevant tests.

## License

This project is licensed under the MIT License.