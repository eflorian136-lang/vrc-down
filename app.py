from flask import Flask, request, redirect
import yt_dlp

app = Flask(__name__)

@app.route('/download')
def download():
    url = request.args.get('url')
    ydl_opts = {
        'format': 'best',
        'quiet': False,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        video_url = info['url']
        
    # Dieser "Header" zwingt den Browser zum Download statt Abspielen
    return redirect(video_url + "&dl=1")

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
