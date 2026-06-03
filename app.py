from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/download')
def download():
    url = request.args.get('url')
    if not url:
        return "Bitte URL angeben: /download?url=DEIN_LINK", 200
    try:
        # Hier versuchen wir die Info zu bekommen
        ydl_opts = {'format': 'best', 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return jsonify({'url': info['url']})
    except Exception as e:
        return f"Fehler: {str(e)}", 500

if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
