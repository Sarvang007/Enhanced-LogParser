import os
import json
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

REPORTS_FILE = os.path.join(os.path.dirname(__file__), "..", "reports", "realtime_metrics.json")

def extract_features(logs):
    """
    Convert raw logs into numerical features for anomaly detection.
    logs = [[timestamp, level, message], ...]
    Features:
      - message_length
      - level_code (INFO=0, WARNING=1, ERROR=2)
    """
    level_map = {"INFO": 0, "WARNING": 1, "ERROR": 2}
    features = []
    for ts, level, msg in logs:
        features.append([
            len(msg),                     # message length
            level_map.get(level.upper(), -1)  # map log level to number
        ])
    return np.array(features)


def detect_anomalies(logs):
    """
    Train IsolationForest and predict anomalies.
    Returns dataframe with anomaly flag.
    """
    if not logs:
        print("⚠️ No logs to analyze")
        return pd.DataFrame()

    X = extract_features(logs)

    # Train IsolationForest
    model = IsolationForest(contamination=0.1, random_state=42)
    preds = model.fit_predict(X)  # -1 = anomaly, 1 = normal

    df = pd.DataFrame(logs, columns=["timestamp", "level", "message"])
    df["anomaly"] = preds
    return df


def run_anomaly_detection():
    """
    Load logs from realtime_metrics.json and run anomaly detection.
    """
    if not os.path.exists(REPORTS_FILE):
        print("⚠️ Metrics file not found. Run ingestion first.")
        return

    with open(REPORTS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    logs = data.get("logs", [])
    df = detect_anomalies(logs)

    if not df.empty:
        anomalies = df[df["anomaly"] == -1]
        print("\n🚨 Detected anomalies:")
        print(anomalies[["timestamp", "level", "message"]])
    else:
        print("✅ No anomalies detected.")


if __name__ == "__main__":
    run_anomaly_detection()
