import json
import re
import os 
import time
import threading
import random
from queue import Queue

from metrics import calculate_metrics
from parser import save_to_csv
from correlation import detect_bruteforce_and_success   # ✅ Import correlation engine

log_queue = Queue()
all_logs = []
LEVELS = ["INFO", "ERROR", "WARNING"]
log_pattern = re.compile(r"(\S+ \S+) (\w+) (.+)")

def producer(log_file=None, max_logs=10):
    """
    If log_file is provided → read file line by line with delay
    Else → generate random logs continuously
    """
    count = 0
    if log_file and os.path.exists(log_file):
        with open(log_file, "r") as f:
            for line in f:
                log_queue.put(line.strip())
                print(f"Produced: {line.strip()}")
                time.sleep(1)
    
    else:
        while count < max_logs:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            level = random.choice(LEVELS)
            message = f"Simulated message at {timestamp}"
            log_line = f"{timestamp} {level} {message}"
            log_queue.put(log_line)  
            print(f"Produced: {log_line}")
            time.sleep(1)
            count += 1


def consumer():
    reports_dir = os.path.join(os.path.dirname(__file__), "..", "reports")
    os.makedirs(reports_dir, exist_ok=True)
    json_path = os.path.join(reports_dir, "realtime_metrics.json")
    alerts_path = os.path.join(reports_dir, "correlation_alerts.json")

    while True:
        log_line = log_queue.get()
        if log_line is None:
            break
        
        match = log_pattern.match(log_line)
        if match:
            timestamp, level, message = match.groups()
            all_logs.append([timestamp, level, message])

            if len(all_logs) > 1000:
                all_logs.pop(0)

        metrics = calculate_metrics(all_logs)

        # ✅ Run correlation engine
        alerts = detect_bruteforce_and_success(all_logs)

        # ✅ Save metrics + logs + alerts together
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump({
                "total_logs": metrics["total_logs"],
                "level_counts": metrics["level_counts"],
                "error_rate": metrics["error_rate"],
                "logs": all_logs,
                "alerts": alerts
            }, f, indent=4)

        # ✅ Save alerts separately
        with open(alerts_path, "w", encoding="utf-8") as f:
            json.dump(alerts, f, indent=4)

        print("\n📊 Live Metrics Updated:")
        print(f"   Total logs: {metrics['total_logs']}")
        print(f"   Logs by level: {metrics['level_counts']}")
        print(f"   Error rate: {metrics['error_rate']}%")

        # 🔔 Print alerts
        if alerts:
            print("🚨 Correlation Alerts:")
            for alert in alerts:
                print(f"   ⚡ {alert}")

        log_queue.task_done()


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(script_dir, "..", "logs", "sample.log")

    producer_thread = threading.Thread(target=producer, args=(log_file,))
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.daemon = True
    consumer_thread.daemon = True

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    print("✅ Real-time ingestion simulation completed")
