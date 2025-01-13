# Overview
This is a personal project primarily created to learn the structure for passing arguments to `yt-dlp`, learning the usage of `subprocess.run()` to run commands in `cmd` from python, and learning to call a python script from `cmd` using a `.bat` file.

The result is a an application to download an audio stream from a given URL. And transcode (convert) it to another audio format, if required.

# External Tools and Packages
`audio-downloader` uses `yt-dlp` for 
- Analysing the different streams
- Downloading chosen audio stream

`audio-downloader` uses `ffmpeg` for
- Transcoding between audio formats

# Installing Repository and Dependencies
- Ensure you have `git` installed
- Ensure you have `python` installed, the recommended version is `Python 3.12.1`
- Clone the repository via `git clone https://github.com/scarletti-ben/audio-downloader`
- Enter the repository via `cd .\audio-downloader\`
- Set up the virtual environment
  -  Initialise the virtual environment via `python -m venv venv`
  -  Activate the virtual environment via `.\venv\Scripts\activate`
- Install required packages via `pip install -r requirements.txt`

### Installing `ffmpeg`
- Find the releases [here](https://www.gyan.dev/ffmpeg/builds/#release-builds)
    - Download `ffmpeg-release-essentials.7z` or `ffmpeg-release-essentials.zip`
    - Extract and rename extracted folder to `ffmpeg`
    - Move the `ffmpeg` folder to the same directory as this `README.md`
- Ensure that you now have the three files at the locations listed below
    - `ffmpeg/bin/ffmpeg.exe`
    - `ffmpeg/bin/ffplay.exe`
    - `ffmpeg/bin/ffprobe.exe`

# Running the Application

### Running the Application via `main.py`
With the virtual environment active, run `python main.py`, you can pass one or two arguments

- The first argument is URL eg. `https://www.website.com/video`
- The second argument is the extension eg. `mp3` or `flac`, do not include the period `.` in the extension

Example commands `python main.py https://www.website.com/video` or `python main.py https://www.website.com/video mp3`

### Running the Application via `audio-downloader.bat`
By default you can run the `batch` (`.bat`) file with arguments from the repository via `C:\...\audio-downloader> audio-downloader` in much the same way as [`main.py`](#running-the-application-via-mainpy)

In order to extend this functionality so that you can run it from anywhere via `C:\> audio-downloader`, and not just from this repository, you can add the repository to your user `PATH` in `System Environment Variables`

#### Adding Repository to User Path
- Navigate to `System Properties`
- Press the `Environment Variables` button near the bottom on the right
- Click on `Path` in the `User variables for user` section at the top
- Press the `Edit` button below
- Press the `New` button on the right
- Type in `C:\...\audio-downloader` and hit enter, making sure to change it to the correct location of the installed repository