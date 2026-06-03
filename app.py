from flask import Flask, request, redirect
import yt_dlp

app = Flask(__name__)

@app.route('/')
def home():
    return "Server läuft! Nutze /download?url=DEIN_TWITCH_LINK zum Herunterladen."

@app.route('/download')
def download():
    url = request.args.get('url')
    if not url:
        return "Bitte eine URL angeben: /download?url=URL", 400
    
    # yt-dlp Optionen mit Browser-Identität (User-Agent)
    ydl_opts = {
        'format': 'best',
        'quiet': False,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info['url']
        return redirect(video_url)
    except Exception as e:
        return f"Fehler beim Download: {str(e)}", 500

if __name__ == '__main__':
    app.run()
