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
    
    ydl_opts = {'format': 'best', 'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        video_url = info['url']
        
    return redirect(video_url)

if __name__ == '__main__':
    app.run()
