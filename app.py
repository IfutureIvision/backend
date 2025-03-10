from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Camera configuration for multiple cameras
CAMERAS = {
    "CAM_1": {
        "ip": "192.168.0.50",
        "port": "8087",
        "url": "http://192.168.0.50:8087/?page=Image&view=ImageWithGraphics",
    },
    "CAM_2": {
        "ip": "192.168.0.12",
        "port": "8087",
        "url": "http://192.168.0.12:8087/?page=Image&view=ImageWithGraphics",
    }
}

# Function to check camera status
def check_camera_status(camera_url):
    try:
        response = requests.get(camera_url, timeout=3)
        return "ONLINE" if response.status_code == 200 else "OFFLINE"
    except requests.exceptions.RequestException:
        return "OFFLINE"


@app.route("/dashboard")
def dashboard():
    camera_status = {
        cam_name: {
            "status": check_camera_status(cam_info["url"]),
            "ip": cam_info["ip"],
            "port": cam_info["port"],
            "url": cam_info["url"]
        }
        for cam_name, cam_info in CAMERAS.items()
    }
    return jsonify(camera_status)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
