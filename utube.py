from pytube import YouTube
from tqdm import tqdm
import sys
import urllib.request
import os

def get_video():
    """
    Retrieve video details and display available resolutions.
    """
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    print(f"Length: {round(yt.length / 60, 2)} mins")

    resolutions = []
    for i, stream in enumerate(yt.streams.filter(file_extension="mp4").order_by('resolution'), start=1):
        resolutions.append(stream)
        print(f"{i}. {stream.resolution}: {stream.filesize / (1024 * 1024):.2f} MB")

    return resolutions

def save_video(resolutions):
    """
    Download the selected video in the chosen resolution.
    """
    try:
        index = int(input("Choose resolution: "))
        chosen_resolution = resolutions[index - 1]
        print(f"Downloading {chosen_resolution.resolution}...")

        # Use a valid file name by replacing invalid characters
        file_name = "".join([c for c in yt.title if c.isalnum() or c.isspace()]).rstrip()
        file_path = os.path.join('./ytvids/', f"{file_name}.mp4")

        # Download the video using urllib.request.urlretrieve
        urllib.request.urlretrieve(chosen_resolution.url, file_path, reporthook=download_progress)
        print("\nDownloaded Successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid index.")
        sys.exit()
    except IndexError:
        print("Invalid index. Please choose a valid resolution index.")
        sys.exit()

def download_progress(count, block_size, total_size):
    """
    Display download progress using tqdm.
    """
    downloaded = count * block_size
    percent = (downloaded / total_size) * 100
    tqdm.write(f"  {percent:.1f}% downloaded", end='\r')

def main():
    """
    Main function to execute the script.
    """
    try:
        resolutions = get_video()
        confirm = input("Confirm download? (y/n): ").strip().lower()
        if not confirm or confirm == "y":
            save_video(resolutions)
        elif confirm == "n":
            print("Download Cancelled")
    except Exception as e:
        print("An Error Occurred!")
        print(e)

if __name__ == "__main__":
    try:
        link = input("Enter video link: ")
        yt = YouTube(link)
        main()
    except KeyboardInterrupt:
        print("\nExiting.....")
        sys.exit()
