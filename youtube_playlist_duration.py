from pytube import Playlist, YouTube
import re
from datetime import timedelta
from tqdm import tqdm

# Ask user for YouTube playlist URL
playlist_url = input("Enter YouTube playlist URL: ")

# Extract playlist ID from URL
playlist_id = re.findall(r"(?<=list=)[^&$]+", playlist_url)[0]

# Initialize playlist object
playlist = Playlist(f"https://www.youtube.com/playlist?list={playlist_id}")

print("Processing playlist...")

# Initialize variables
total_duration = 0
num_processed = 0

# Loop through each video in playlist
for url in tqdm(playlist.video_urls):
    yt = YouTube(url)
    if yt:
        duration = yt.length
        total_duration += duration
        num_processed += 1
    else:
        print(f"Could not process video: {url}")

# Format total duration
total_duration = str(timedelta(seconds=total_duration))

# Print total duration
print(f"Total duration: {total_duration}")
