# Command-Line YouTube Video Downloader for Android and PC

This is a simple command-line tool for downloading YouTube videos in various resolutions. It uses the Pytube library to interact with the YouTube API and the tqdm library to display download progress.
This tool runs on both PC and Android terminal emulators.

## Installation

1. Clone this repository to your local machine.
	git clone https://github.com/LouisdeMagician/utube
	
2. Install the required dependencies using pip:
	pip install -r requirements.txt

## Notes

**For Android, this program was tested on `Termux` terminal emulator app.**
**`utube.py` creates a directory `ytvids` by default, where downloaded videos are stored.**
**This program is not able to download Youtube age restricted content.**
**Interruption of internet connection during download process will result in a failed download.**
**Edit `utube.py` file and cutomize video storage `path` if desired.**

## Usage

1. Run the program by executing the `utube.py` script.
2. Enter the YouTube video link when prompted.
3. Choose the desired video resolution from the available options.
4. Confirm the download when prompted.
5. The video will be downloaded to the `path` directory with a sanitized file name.

## Requirements

- Python 3.x
- pytube
- tqdm

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
