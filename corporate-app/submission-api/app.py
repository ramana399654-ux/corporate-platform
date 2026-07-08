from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/submission")
def submission():
    return jsonify({
        "service": "submission-api",
        "pod": socket.gethostname()
    })

@app.route("/")
def home():
    return jsonify({
        "message": "Submission API running",
        "pod": socket.gethostname()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
