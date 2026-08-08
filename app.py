from flask import Flask, request, jsonify
from extractor import get_video_info

app = Flask(__name__)

@app.route('/api/video', methods=['GET'])
def video_api():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"error": "URL parameter is required"}), 400
    
    data = get_video_info(video_url)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
