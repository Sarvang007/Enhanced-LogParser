import os
import re
from parser import save_to_csv
from metrics import calculate_metrics, save_summary,save_structure_report
from visualize import plots_logs_by_level,plot_error_rate

def parse_log(file_path):
    if not os.path.exists(file_path):
        print(f"File not found,{file_path}")
        return []
    
    logs=[]
    with open(file_path,"r")as f:
            for line in f:
                 match=re.match(r"(\S+ \S+) (\w+) (.+)",line)
                 if match:
                      timestamp,level,message=match.groups()
                      logs.append([timestamp,level,message])

               

    if logs:
         save_to_csv(logs)
         print(f"✅Parsed {len(logs)} and saves to reports/output.csv")
         metrics = calculate_metrics(logs)
         print("\n📊 Log Metrics:")
         print(f"   Total logs: {metrics['total_logs']}")
         print(f"   Logs by level: {metrics['level_counts']}")
         print(f"   Error rate: {metrics['error_rate']}%")

         save_summary(metrics)
         save_structure_report(logs,metrics)

         plots_logs_by_level(metrics["level_counts"])
         plot_error_rate(metrics["error_rate"])
    else:
         print("⚠️NO logs matched the intended pattern")

    return logs

if __name__=="__main__":
     script_dir=os.path.dirname(os.path.abspath(__file__))
     log_file=os.path.join(script_dir,"..",'logs','sample.log')
     parse_log(log_file)