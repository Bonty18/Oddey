from flask import Flask, render_template, jsonify
from ytmusicapi import YTMusic
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# This single line now handles the login by reading the browser.json file.
ytmusic = YTMusic("browser.json")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/library/playlists')
def get_library_playlists():
    try:
        playlists = ytmusic.get_library_playlists()
        return jsonify(playlists)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/stream/<video_id>')
def get_stream_url(video_id):
    try:
        stream_url = ytmusic.get_streaming_data(video_id)['formats'][0]['url']
        return jsonify({"url": stream_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 81)))
    
