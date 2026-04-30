# 🛡️ Linux Log Analysis, Automation & SIEM Visualisation

A custom Python-based SIEM (Security Information and Event Management) system built from scratch — ingesting live Linux auth logs, detecting threats automatically, and visualising real-time security events on a Flask dashboard.

> **Target Roles:** SOC Analyst · SIEM Engineer · Threat Analyst · **$70K–$170K**

---

## 📸 Dashboard Preview

![SIEM Dashboard](dashboard_preview.png)

---

## 🎯 Project Overview

This project mirrors real-world SOC Tier-1 workflows:

```
Linux Logs  →  Python Parser  →  Threat Detector  →  Flask Dashboard
/var/log/       regex rules       brute force          real-time UI
auth.log         27+ events        3 alerts             charts + tables
```

---

## ✅ Features

| Feature | Description |
|---|---|
| 📥 Log Collection | Reads live `/var/log/auth.log` and `/var/log/syslog` |
| 🔍 Log Parsing | Regex-based detection of SSH, sudo, and login events |
| 🚨 Threat Detection | Brute force (HIGH) and privilege escalation (MEDIUM) alerts |
| 📊 Flask Dashboard | Real-time UI with Chart.js bar charts and alerts table |
| 🔄 Auto-Refresh | Dashboard updates every 30 seconds automatically |
| 💾 JSON Storage | Structured event and alert storage in JSON format |

---

## 🧱 Tech Stack

- **Language:** Python 3
- **Web Framework:** Flask
- **Frontend:** HTML, CSS, Chart.js
- **Log Analysis:** Python `re` (regex), `collections.Counter`
- **Scripting:** Bash, Linux CLI
- **Storage:** JSON files
- **OS:** Ubuntu / WSL (Windows Subsystem for Linux)

---

## 📁 Project Structure

```
siem-project/
├── app.py                  # Flask web server & API routes
├── log_collector.py        # Reads Linux log files
├── log_parser.py           # Parses events using regex
├── threat_detector.py      # Detection rules & alert generation
├── templates/
│   └── dashboard.html      # SIEM dashboard UI
├── static/                 # Static assets
└── data/
    ├── events.json         # Parsed security events
    └── alerts.json         # Generated threat alerts

## 🧠 Skills Demonstrated

- **Log Parsing** — regex-based structured event extraction from raw log files
- **Event Correlation** — linking multiple events across time to detect attack patterns
- **Scripting Automation** — Python scripts for log ingestion, parsing, and detection
- **SIEM Workflows** — end-to-end pipeline from raw logs to actionable alerts
- **Detection Engineering** — building threshold-based rules for brute force and escalation
- **Security Telemetry** — operationalising log data into a visual security dashboard
---

## 🔮 Future Improvements

- [ ] Email/SMS alerts when HIGH severity threat is detected
- [ ] Auto-block attacker IPs using `iptables`
- [ ] SQLite database for proper event storage and querying
- [ ] GeoIP mapping to visualise attacker locations on a world map
- [ ] Deploy online with a public URL using Railway or Render



This project is open source and available under the [MIT License](LICENSE).
