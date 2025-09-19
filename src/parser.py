import csv

def save_to_csv(logs, output_file="reports/output.csv"):
    with open(output_file,"w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["timestamps","level","message"])
        for logs in logs:
            writer.writerow(logs)
