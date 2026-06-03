from flask import Flask, request, redirect
import yt_dlp
import sys

app = Flask(__name__)

@app.route('/download')
def download():
    url = request.args.get('url')
    if not url:
        return "Fehler: Keine URL angegeben.", 400
    
    ydl_opts = {
        'format': 'best',
        'quiet': False
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info['url']
        return redirect(video_url)
    except Exception as e:
        return f"Download-Fehler: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
