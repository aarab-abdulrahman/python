import yt_dlp
import os

def download_video(url, destination=r"C:\Users\group2\Downloads\python"):
    try:
        if not os.path.exists(destination):
            os.makedirs(destination)

        ydl_opts = {
            'outtmpl': f'{destination}/%(title)s.%(ext)s',  
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"Video downloaded successfully to {destination}")
    
    except Exception as e:
        print(f"Error downloading video: {e}")

# Example usage
url = input("Enter YouTube video link: ").strip()  
destination = r"C:\Users\Downloads"  
download_video(url, destination)
