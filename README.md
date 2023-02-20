# YouTube Playlist Duration Calculator

This script calculates the total duration of a YouTube playlist. It uses the `pytube` library to fetch the duration of each video in the playlist and sums them up to give the total duration of the playlist.

## Prerequisites

Before running the script, make sure you have the following prerequisites installed:

- Python 3.x
- pytube library (you can install it using `pip install pytube`)

## Usage

To use the script, follow these steps:

1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory where you saved the script.
3. Run the script using the command `python youtube_playlist_duration.py`.
4. When prompted, enter the URL of the YouTube playlist you want to calculate the duration for.

The script will then fetch the duration of each video in the playlist and sum them up to give the total duration of the playlist.

## Output

The script outputs the total duration of the playlist in the format `HH:MM:SS`. It also shows a progress bar indicating the percentage of videos processed.

Example output:

Processing playlist...
[=================== ] 90%
Total duration: 01:23:45


## Note

This script may take some time to run depending on the number of videos in the playlist.
