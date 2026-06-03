from flask import Flask, request, redirect
import yt_dlp

app = Flask(__name__)

@app.route('/download')
def download():
    url = request.args.get('url')
    if not url:
        return "Keine URL angegeben", 400
    
    # yt-dlp holt die direkte Stream-URL von Twitch
    ydl_opts = {'format': 'best', 'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        video_url = info['url']
        
    return redirect(video_url)

if __name__ == '__main__':
    app.run()
