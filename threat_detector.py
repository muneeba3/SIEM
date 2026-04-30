import json
from collections import Counter

BRUTE_FORCE_THRESHOLD = 5

def load_events():
    try:
        with open("data/events.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def detect_brute_force(events):
    alerts = []
    failed = [e for e in events if e["type"] == "failed_ssh"]
    ip_counts = Counter(e["ip"] for e in failed)
    for ip, count in ip_counts.items():
        if count >= BRUTE_FORCE_THRESHOLD:
            alerts.append({
                "severity": "HIGH",
                "type": "Brute Force Detected",
                "ip": ip,
                "attempts": count,
                "message": f"{count} failed SSH attempts from {ip}"
            })
    return alerts

def detect_privilege_escalation(events):
    alerts = []
    sudo_events = [e for e in events if e["type"] == "sudo_use"]
    if len(sudo_events) > 10:
        alerts.append({
            "severity": "MEDIUM",
            "type": "High sudo activity",
            "message": f"{len(sudo_events)} sudo commands executed"
        })
    return alerts

def run_detection():
    events = load_events()
    alerts = []
    alerts += detect_brute_force(events)
    alerts += detect_privilege_escalation(events)
    with open("data/alerts.json", "w") as f:
        json.dump(alerts, f, indent=2)
    print(f"[!] {len(alerts)} alerts generated")
    return alerts
