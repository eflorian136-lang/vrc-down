import os
import yt_dlp
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/download')
def download():
    url = request.args.get('url')
    if not url:
        return "Bitte URL angeben: /download?url=DEIN_TWITCH_LINK", 200
    
    try:
        ydl_opts = {'format': 'best', 'quiet': False}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info['url']
        return redirect(video_url)
    except Exception as e:
        return f"Fehler: {str(e)}", 500

# WICHTIG: Gunicorn braucht das hier nicht, 
# aber wir stellen sicher, dass Flask nicht auf einem festen Port klebt
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
