# from flask import Flask, render_template, jsonify
# import requests

# app = Flask(__name__)

# # Camera configuration
# CAMERA_IP = "192.168.0.11"
# PORT = "8087"
# CAMERA_URL = f"http://{CAMERA_IP}:{PORT}/?page=Image&view=ImageWithGraphics"

# # Function to check camera status
# def check_camera_status():
#     try:
#         response = requests.get(CAMERA_URL, timeout=3)
#         if response.status_code == 200:
#             return "Connected"
#     except requests.exceptions.RequestException:
#         return "Disconnected"
#     return "Disconnected"

# @app.route("/")
# def index():
#     return render_template("index.html", camera_ip=CAMERA_IP, port=PORT, camera_url=CAMERA_URL)

# @app.route("/status")
# def status():
#     return jsonify({
#         "status": check_camera_status(),
#         "camera_ip": CAMERA_IP,
#         "port": PORT
#     })

# if __name__ == "__main__":
#     app.run(debug=True)




# ##serial number search
# import subprocess
# import json
# import time
# import webbrowser
# import os
# from flask import Flask, render_template, jsonify

# app = Flask(__name__)

# # Camera configuration
# CAMERA_IP = "192.168.0.11"
# PORT = "8087"
# CAMERA_URL = f"http://{CAMERA_IP}:{PORT}/?page=Image&view=ImageWithGraphics"

# # Load valid serial numbers from JSON
# def load_valid_serials():
#     with open("valid_serials.json", "r") as f:
#         data = json.load(f)
#         return data["valid_serials"] if isinstance(data, dict) and "valid_serials" in data else data

# # Function to get the serial number by running serial_number.py
# def get_detected_serial():
#     try:
#         subprocess.run(["python", "serial_number.py"], timeout=10)
#         if os.path.exists("serial_output.txt"):
#             with open("serial_output.txt", "r") as f:
#                 serial_number = f.read().strip()
#                 return serial_number
#     except Exception as e:
#         print(f"Error running serial_number.py: {e}")
#     return None

# # Function to check if serial number is valid
# def is_valid_serial(serial_number):
#     valid_serials = load_valid_serials()
#     return serial_number in valid_serials

# # Function to check camera status
# def check_camera_status():
#     detected_serial = get_detected_serial()
#     return "Connected" if detected_serial and is_valid_serial(detected_serial) else "Disconnected"

# @app.route("/")
# def index():
#     return render_template("index.html", camera_ip=CAMERA_IP, port=PORT, camera_url=CAMERA_URL)

# @app.route("/status")
# def status():
#     detected_serial = get_detected_serial()
#     connection_status = "Connected" if detected_serial and is_valid_serial(detected_serial) else "Disconnected"

#     return jsonify({
#         "serial_number": detected_serial if detected_serial else "Not Detected",
#         "status": connection_status,
#         "camera_ip": CAMERA_IP,
#         "port": PORT
#     })

# # Open the browser only once after fetching the serial number
# def open_camera_page():
#     detected_serial = get_detected_serial()
#     if detected_serial and is_valid_serial(detected_serial):
#         webbrowser.open(CAMERA_URL)

# if __name__ == "__main__":
#     # Start serial number script once before opening the browser
#     detected_serial = get_detected_serial()

#     # Open the camera page only if serial number is valid
#     if detected_serial and is_valid_serial(detected_serial):
#         time.sleep(2)  # Give some time before opening the browser
#         webbrowser.open(CAMERA_URL)

#     app.run(debug=False, use_reloader=False)




from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Camera configuration for multiple cameras
CAMERAS = {
    "CAM_1": {
        "ip": "192.168.0.11",
        "port": "8087",
        "url": "http://192.168.0.11:8087/?page=Image&view=ImageWithGraphics",
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

@app.route("/")
def index():
    return render_template("index.html", cameras=CAMERAS)

@app.route("/status")
def status():
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
    app.run(debug=True, host="0.0.0.0")
