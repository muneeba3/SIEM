from flask import Flask, render_template, jsonify
from log_parser import parse_logs
from threat_detector import run_detection
import json, os

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/events")
def get_events():
    try:
        with open("data/events.json") as f:
            return jsonify(json.load(f))
    except FileNotFoundError:
        return jsonify([])

@app.route("/api/alerts")
def get_alerts():
    try:
        with open("data/alerts.json") as f:
            return jsonify(json.load(f))
    except FileNotFoundError:
        return jsonify([])

@app.route("/api/refresh")
def refresh():
    parse_logs()
    run_detection()
    return jsonify({"status": "refreshed"})

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    parse_logs()
    run_detection()
    app.run(debug=True, host="0.0.0.0", port=5000)
