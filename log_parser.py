import re, json
from log_collector import collect_all

PATTERNS = {
    "failed_ssh": re.compile(
        r"(\w+\s+\d+ \d+:\d+:\d+).+Failed password for (\S+) from (\d+\.\d+\.\d+\.\d+)"
    ),
    "success_ssh": re.compile(
        r"(\w+\s+\d+ \d+:\d+:\d+).+Accepted password for (\S+) from (\d+\.\d+\.\d+\.\d+)"
    ),
    "sudo_use": re.compile(
        r"(\w+\s+\d+ \d+:\d+:\d+).+sudo.+COMMAND=(.+)"
    ),
}

def parse_logs():
    raw = collect_all()
    events = []

    for line in raw.get("auth", []):
        for event_type, pattern in PATTERNS.items():
            match = pattern.search(line)
            if match:
                event = {
                    "type": event_type,
                    "timestamp": match.group(1),
                    "raw": line.strip()
                }
                if event_type in ("failed_ssh", "success_ssh"):
                    event["user"] = match.group(2)
                    event["ip"] = match.group(3)
                events.append(event)

    with open("data/events.json", "w") as f:
        json.dump(events, f, indent=2)

    print(f"[+] Parsed {len(events)} events")
    return events
