
# < ========================================================
# < Imports
# < ========================================================

import subprocess
import sys

# < ========================================================
# < Settings
# < ========================================================

ffmpeg_path: str = "ffmpeg/bin/ffmpeg.exe"
output_format: str = './downloads/%(title)s.%(ext)s'

# < ========================================================
# < Execution
# < ========================================================

if __name__ == "__main__":

    arguments: list[str] = sys.argv
    quantity: int = len(arguments)

    if quantity == 1:
        raise UserWarning("Please provide a URL as the first argument")
    elif quantity == 2:
        url = arguments[1]
        extension = ''
    elif quantity == 3:
        url = arguments[1]
        extension = arguments[2]
    elif quantity > 3:
        raise UserWarning("Too many arguments provided")
    
    command: list[str] = [
        sys.executable, '-m', 'yt_dlp',         # < Run yt_dlp with python from the current environment
        '--format', 'bestaudio',                # < Download best audio stream, no fallback
        '--continue',                           # < Resume interrupted downloads
        '--ignore-errors',                      # < Skip videos with errors
        '--no-overwrites',                      # < Don't overwrite existing files
        '--output', output_format,              # < Ensure filename matches video title
        '--verbose',                            # < Show detailed output / logging
        '--extract-audio',                      # < Extract audio stream only
        '--restrict-filenames',                 # < Ensure only safe characters in filenames
        '--ffmpeg-location', ffmpeg_path,       # < Provide the path to ffmpeg for transcoding and for --extract-audio flag
        url                                     # < Link to the video to be downloaded
    ]

    if extension:
        transcode: list[str] = [
            '--audio-quality', '0',             # < Ensure highest quality for lossy transcoding
            '--audio-format', extension,        # < Format to be transcoded to, if not already in said format
        ]
        command.extend(transcode)

    subprocess.run(command)