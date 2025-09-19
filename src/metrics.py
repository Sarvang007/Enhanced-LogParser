import os
import csv
import json
from collections import Counter

def calculate_metrics(logs):
    """
    Calculate metrics from parsed logs.
    logs = list of [timestamp, level, message]
    """
    total_logs=len(logs)
    levels=[log[1] for log in logs]
    level_count=Counter(levels)

    error_count=level_count.get("Error",0)
    error_rate=(error_count/total_logs)*100 if total_logs>0 else 0

    metrics={
        "total_logs": total_logs,
        "level_counts": dict(level_count),
        "error_rate": round(error_rate,2)
    }

    return metrics

def save_summary(metrics):
    reports_dir=os.path.join(os.path.dirname(__file__),"..","reports")
    os.makedirs(reports_dir,exist_ok=True)
    output_file=os.path.join(reports_dir,"summary.txt")

    with open(output_file,"w",encoding="utf-8") as f:
        f.write("📊 Log Analysis Summary\n")
        f.write("=========================\n\n")
        f.write(f"Total logs: {metrics['total_logs']}\n")
        f.write(f"Logs by level: {metrics['level_counts']}\n")
        f.write(f"Error rate: {metrics['error_rate']}%\n")

    print(f"Summary saved to {output_file}")

def save_structure_report(logs,metrics):
    """
    Save parsed logs and metrics into CSV and JSON structured reports.
    """
    reports_dir=os.path.join(os.path.dirname(__file__),"..","..","reports")
    os.makedirs(reports_dir,exist_ok=True)

    # save metrics to json
    json_file=os.path.join(reports_dir,"structured_report.json")
    with open(json_file,"w",encoding="utf-8") as f:
        json.dump({
            "metrics": metrics,
            "logs": logs
        },f,indent=4)
        print(f"✅ JSON structured report saved to {json_file}")

    # save logs + metrics to csv
    csv_file=os.path.join(reports_dir,"structured_report.csv")
    with open(csv_file,"w",encoding="utf-8")as f:
        writer=csv.writer(f)
        # writer.writerow(["Metric","Value"])
        # for key,value in metrics.items():
        #     writer.writerow([key,value])
        # writer.writerow([])
        # write logs
        writer.writerow(["Timestamp","Levels","Message"])
        for log in logs:
            writer.writerow(logs)
        print(f"✅ CSV structured report saved to {csv_file}")