import requests
import subprocess
import sys

API_URL = "https://vrc-down.onrender.com/download"

def download_twitch_video(twitch_url):
    print(f"Hole Download-URL für: {twitch_url}...")
    response = requests.get(API_URL, params={'url': twitch_url})
    
    if response.status_code == 200:
        data = response.json()
        video_url = data.get('url')
        print(f"Starte Download von: {video_url}")
        subprocess.run(["yt-dlp", video_url, "-o", "twitch_video.mp4"])
        print("Download abgeschlossen!")
    else:
        print("Fehler: Server konnte keine URL generieren.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        download_twitch_video(sys.argv[1])
    else:
        print("Bitte eine Twitch-URL angeben: python downloader.py [URL]")
