# © 2025 Fr0zst. All rights reserved. 
# Unauthorized copying prohibited.

import os
from pytubefix import YouTube
from moviepy.editor import AudioFileClip

def get_downloads_path():
    """Returns the path to the user's Downloads folder."""
    if os.name == 'nt':  # For Windows
        import winreg
        try:
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                downloads_path = winreg.QueryValueEx(key, downloads_guid)[0]
            return downloads_path
        except Exception:
            return os.path.join(os.path.expanduser('~'), 'Downloads')
    else:  # For macOS, Linux, etc.
        return os.path.join(os.path.expanduser('~'), 'Downloads')

def download_youtube_media(url, file_format):
    """Downloads a YouTube video or audio to the Downloads folder."""
    downloads_path = get_downloads_path()

    try:
        yt = YouTube(url)
        print(f"\nTitle: {yt.title}")
        print("Fetching streams...")

        if file_format == "mp4":
            # For MP4, get the highest resolution stream
            stream = yt.streams.get_highest_resolution()
            if stream:
                print("Downloading video as MP4...")
                stream.download(output_path=downloads_path)
                print(f"Downloaded '{yt.title}' to {downloads_path}")
            else:
                print("No suitable MP4 stream found.")
        
        elif file_format == "mp3":
            # For MP3, get the highest quality audio stream and convert
            audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
            if audio_stream:
                print("Downloading audio stream...")
                # Download the audio file to a temporary location
                temp_file = audio_stream.download(output_path=downloads_path)
                
                # Convert to MP3 using moviepy
                base, ext = os.path.splitext(temp_file)
                mp3_file = base + '.mp3'
                
                audio_clip = AudioFileClip(temp_file)
                audio_clip.write_audiofile(mp3_file)
                audio_clip.close()
                
                # Remove the original downloaded file
                os.remove(temp_file)
                
                print(f"Downloaded audio '{yt.title}' as MP3 to {downloads_path}")
            else:
                print("No suitable audio stream found.")

    except Exception as e:
        print(f"An error occurred: {e}")
        # Offer troubleshooting steps for common errors
        print("\nPossible solutions:")
        print("1. The video may be region-restricted or unavailable. Try another link.")
        print("2. Update the pytubefix library by running: `pip install --upgrade pytubefix`")
        print("3. Ensure your moviepy library is compatible by running: `pip install moviepy==1.0.3`")


if __name__ == "__main__":
    banner = r"""
               



                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣦⣤⣴⣤⣤⣄⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣛⣻⣿⣦⣀⠀⢀⣀⣀⣏⣹⠀
⢠⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠭⠭⠽⠽⠿⠿⠭⠭⠭⠽⠿⠿⠛
⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⢻⣿⣿⣿⡟⠏⠉⠉⣿⢿⣿⣿⣿⣇⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠁⠀⠀⠀⢠⣿⣿⣿⠋⠑⠒⠒⠚⠙⠸⣿⣿⣿⣿⡄⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⡿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    print(banner)
    print("Made By Fr0zsty\n")
    
    link = input("Please paste the YouTube link here: ")

    while True:
        choice = input("Enter 'mp3' or 'mp4' to choose the download format: ").lower()
        if choice in ["mp3", "mp4"]:
            break
        else:
            print("Invalid choice. Please enter 'mp3' or 'mp4'.")

    download_youtube_media(link, choice)


