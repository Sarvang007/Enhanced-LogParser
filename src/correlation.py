import re
from collections import defaultdict
from datetime import datetime, timedelta

# Regex pattern for log lines (customize for your log format)
log_pattern = re.compile(r"(\S+ \S+) (\w+) (.+)")

def parse_timestamp(ts_str):
    """Convert timestamp string -> datetime (adjust format to your logs)."""
    try:
        return datetime.strptime(ts_str, "%H:%M:%S")
    except ValueError:
        return None

def detect_bruteforce_and_success(logs):
    """
    Detect brute force (multiple failed logins) followed by a success.
    logs: list of [timestamp, level, message]
    """
    failed_logins = defaultdict(list)
    alerts = []

    for ts, level, message in logs:
        timestamp = parse_timestamp(ts)
        if not timestamp:
            continue

        # Match failed login
        if "failed login" in message.lower():
            ip_match = re.search(r"IP:([\d\.]+)", message)
            if ip_match:
                ip = ip_match.group(1)
                failed_logins[ip].append(timestamp)

                # Check if 3+ failures within 5 minutes
                recent_failures = [t for t in failed_logins[ip] if timestamp - t <= timedelta(minutes=5)]
                if len(recent_failures) >= 3:
                    alerts.append(f"🚨 Brute Force suspected from {ip} at {timestamp}")

        # Match successful login
        elif "successful login" in message.lower():
            ip_match = re.search(r"IP:([\d\.]+)", message)
            if ip_match:
                ip = ip_match.group(1)
                if ip in failed_logins and len(failed_logins[ip]) >= 3:
                    alerts.append(f"🔥 SUCCESS after brute force from {ip} at {timestamp}")

    return alerts
