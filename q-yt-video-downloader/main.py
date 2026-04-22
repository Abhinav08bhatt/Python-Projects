from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import os
import re


def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)


def download_video(url, save_path):
    try:
        yt = YouTube(
            url,
            on_progress_callback=on_progress
        )

        print(f"\nTitle: {yt.title}")
        print(f"Author: {yt.author}")
        print(f"Length: {yt.length} seconds\n")

        stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()

        if stream is None:
            print("No downloadable MP4 stream found.")
            return

        safe_title = sanitize_filename(yt.title)
        output_file = stream.download(output_path=save_path, filename=safe_title + ".mp4")

        print(f"\nDownload complete!")
        print(f"Saved to: {output_file}")

    except Exception as e:
        print(f"Error: {e}")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    downloaded = total_size - bytes_remaining
    percent = downloaded / total_size * 100

    print(f"\rDownloading... {percent:.2f}% complete", end="")


def open_file_dialog():
    folder = filedialog.askdirectory(title="Select Download Folder")
    return folder


def main():
    root = tk.Tk()
    root.withdraw()

    video_url = input("Enter a YouTube URL: ").strip()

    if not video_url.startswith("http"):
        print("Invalid URL.")
        return

    save_dir = open_file_dialog()

    if not save_dir:
        print("No folder selected. Exiting.")
        return

    print("\nStarting download...")
    download_video(video_url, save_dir)


if __name__ == "__main__":
    main()
