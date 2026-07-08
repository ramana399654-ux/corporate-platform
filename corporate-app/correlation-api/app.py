from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/correlation")
def correlation():
    return jsonify({
        "service": "correlation-api",
        "pod": socket.gethostname()
    })

@app.route("/")
def home():
    return jsonify({
        "message": "Correlation API running",
        "pod": socket.gethostname()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
