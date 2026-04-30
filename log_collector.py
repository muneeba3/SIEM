import re, json

LOG_FILES = {
    "auth": "/var/log/auth.log",
    "syslog": "/var/log/syslog",
}

def read_log(path):
    try:
        with open(path, "r", errors="ignore") as f:
            return f.readlines()
    except PermissionError:
        print(f"[!] Permission denied: {path}. Run with sudo.")
        return []
    except FileNotFoundError:
        print(f"[!] File not found: {path}")
        return []

def collect_all():
    raw = {}
    for name, path in LOG_FILES.items():
        raw[name] = read_log(path)
    return raw
