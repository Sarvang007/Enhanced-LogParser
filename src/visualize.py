import os
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
from datetime import datetime

def plots_logs_by_level(level_counts):
    """
    Generate a bar chart showing number of logs by level.
    """
    output_dir=os.path.join(os.path.dirname(__file__),"..","reports","plots")
    os.makedirs(output_dir,exist_ok=True)

    levels=list(level_counts.keys())
    counts=list(level_counts.values())

    plt.figure(figsize=(6,4))
    sns.barplot(x=levels,y=counts,palette="viridis")
    plt.title("Logs by Level")
    plt.xlabel("Log Level")
    plt.ylabel("Count")

    timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path=os.path.join(output_dir,f"logs_by_level_{timestamp}.png")
    plt.savefig(output_path)
    plt.close()
    print(f"📊 Saved plot: {output_path}")


def plot_error_rate(error_rate):
    """
    Generate a pie chart for error rate vs non-error logs.
    """
    output_dir=os.path.join(os.path.dirname(__file__),"..","reports","plots")
    os.makedirs(output_dir,exist_ok=True)

    labels=["Error Logs","Other Logs"]
    sizes=[error_rate,100-error_rate]

    plt.figure(figsize=(5,5))
    plt.pie(sizes,labels=labels,autopct="%1.1f%%", colors=["#e74c3c", "#2ecc71"])
    plt.title("Error Rate Distribution")
    
    timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path=os.path.join(output_dir,f"error_rate_{timestamp}.png")
    plt.savefig(output_path)
    plt.close()
    print(f"📊 Saved plot: {output_path}")