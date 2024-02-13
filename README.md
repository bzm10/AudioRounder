# Audio Rounder

## Introduction

Audio Rounder is a Python script designed to round audio files by looping through them and applying a specified operation.
The script is easy to use with detailed comments in the code explaining what each command does.

## How it Works

The script operates by slightly adjusting the playback speed of audio files to achieve the rounding effect. It utilizes FFmpeg to efficiently manipulate the audio speed. The process involves looping through all the audio files in the specified directory, applying a subtle speed adjustment to round each file as per the defined operation.

## Requirements

Before running the script, ensure that you have the following dependencies installed:

- Python 3
- FFmpeg
- PyDub

#### You can install Python 3 from [Python's official website](https://www.python.org/downloads/), 

### To install FFmpeg:

For mac you need to use [Homebrew](https://brew.sh/):
```bash
brew install ffmpeg
```
For linux you need to use sudo:
```bash
sudo apt install ffmpeg
```
For windows you can follow this [tutorial](https://phoenixnap.com/kb/ffmpeg-windows).

### To install PyDub, you can use the following command:

```bash
pip3 install pydub
```


## Setup

### 1. You need to download this repository
You can use git:
```bash
git clone https://github.com/your-username/your-repository.git
```
### 2. Save it to the same location that has the audio files
```bash
cd repository_location
```
### 3. Run the script from the location that has the audio files
```bash
python3 script.py
```

### The script will place the modified files into the "modified" folder, while the original ones will be placed in the "original" folder.

Feel free to customize the script to suit your specific needs.
