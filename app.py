from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app) # WICHTIG: Erlaubt den Zugriff von deiner Website

@app.route('/get-link')
def get_link():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'Keine URL'}), 400
    
    try:
        ydl_opts = {'format': 'best', 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return jsonify({'stream_url': info['url']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
