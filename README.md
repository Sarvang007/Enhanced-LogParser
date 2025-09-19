# 🚀 Enhanced Log Parser

A powerful Python-based log parsing and reporting tool built for Security Operations Centers (SOC). Analyze syslogs, Windows event logs, and custom application logs with ease, transforming raw data into actionable insights through structured reports, real-time dashboards, and advanced analytics.

## 🌟 Key Features

- **Flexible Log Parsing**: Processes diverse log formats (syslogs, Windows event logs, custom logs).
- **Real-Time Processing**: Ingests and analyzes logs in real-time using lightweight Python queues.
- **Advanced Analytics**: Includes metrics, anomaly detection, and multi-source log correlation.
- **Visualizations**: Generates static charts (bar, pie) and interactive dashboards using Dash/Streamlit.
- **Structured Outputs**: Exports reports in CSV, JSON, and text formats for easy integration.

## 📂 Project Structure

| Path                              | Description                                      |
|-----------------------------------|--------------------------------------------------|
| `src/`                            | Core source code                                 |
| `src/__init__.py`                 | Package initialization                           |
| `src/main.py`                     | Batch log parsing entry point                    |
| `src/parser.py`                   | Log parsing logic                                |
| `src/metrics.py`                  | Metrics calculation and report generation        |
| `src/visualize.py`                | Static visualizations (charts & plots)           |
| `src/realtime_ingestion.py`       | Real-time log ingestion with threading & queue   |
| `src/dashboard.py`                | Interactive Dash/Streamlit dashboard             |
| `src/anomaly_detection.py`        | ML-based anomaly detection                       |
| `src/correlation.py`              | Multi-source log correlation engine              |
| `src/utils.py`                    | Utility functions                                |
| `tests/`                          | Unit tests                                       |
| `tests/__init__.py`               | Test package initialization                      |
| `tests/test_parser.py`            | Parser unit tests                                |
| `reports/`                        | Generated reports and visualizations             |
| `reports/output.csv`              | Raw parsed logs                                  |
| `reports/summary.txt`             | Metrics summary                                  |
| `reports/structured_report.csv`   | Structured CSV report                            |
| `reports/structured_report.json`  | Structured JSON report                           |
| `reports/realtime_metrics.json`   | Real-time metrics (continuously updated)         |
| `reports/plots/`                  | Static visualizations                            |
| `reports/plots/logs_by_level_*.png` | Bar chart of logs by level                     |
| `reports/plots/error_rate_*.png`  | Pie chart of error vs non-error logs            |
| `logs/`                           | Sample log files for testing                     |
| `logs/sample.log`                 | Example log file                                 |
| `.gitignore`                      | Ignored files (venv, pycache, etc.)              |
| `requirements.txt`                | Project dependencies                             |
| `README.md`                       | Project documentation (you're here!)             |

## 📈 Project Progress

### ✅ Phase 1: Foundation

| Step | Task                                      | Status     |
|------|-------------------------------------------|------------|
| 1    | Setup virtual environment & install requirements | ✅ Completed |
| 2    | Create project structure (folders & files) | ✅ Completed |
| 3    | Initialize Git & commit skeleton          | ✅ Completed |
| 4    | Implement basic log parser (reads sample.log, extracts fields) | ✅ Completed |
| 5    | Add unit test for parser                  | ✅ Completed |
| 6    | Generate first report (CSV/JSON output)   | ✅ Completed |

### ✅ Phase 2: Metrics & Visualizations

| Step | Task                                      | Status     |
|------|-------------------------------------------|------------|
| 1    | Implement metrics calculation (total logs, error rates, top IPs) | ✅ Completed |
| 2    | Generate summary report (text output)     | ✅ Completed |
| 3    | Generate CSV/JSON structured report       | ✅ Completed |
| 4    | Implement static visualizations (counts, error trends, top IPs) | ✅ Completed |
| 5    | Save plots automatically in reports/plots/ | ✅ Completed |

### ✅ Phase 3: Real-Time & Advanced Analytics

| Step | Task                                      | Status     |
|------|-------------------------------------------|------------|
| 1    | Real-time ingestion (lightweight Python queue) | ✅ Completed |
| 2    | Stream processing (real-time aggregation) | ✅ Completed |
| 3    | Interactive dashboard (Dash/Streamlit)    | ✅ Completed |
| 4    | Machine learning parsing (anomaly detection) | ✅ Completed |
| 5    | Log correlation engine (multi-source correlation) | ✅ Completed |

## ⚙️ Setup Instructions

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/enhanced-log-parser.git
   cd enhanced-log-parser
# ⚙️ Set Up Virtual Environment  

```bash
python -m venv .venv
Activate:

Windows:

bash
Copy code
.venv\Scripts\activate
Linux/Mac:

bash
Copy code
source .venv/bin/activate
📦 Install Dependencies
bash
Copy code
pip install -r requirements.txt
▶️ Usage
🔹 Run the parser for batch processing:
bash
Copy code
python -m src.main
🔹 For real-time log ingestion and dashboard:
bash
Copy code
python -m src.dashboard
📝 Sample Log Format (logs/sample.log)
text
Copy code
2025-09-04 19:00 INFO User login successful
2025-09-04 19:05 ERROR Failed password attempt
2025-09-04 19:10 WARNING Disk usage 90%
📊 Outputs
📑 Reports
reports/output.csv: Raw parsed logs.

reports/summary.txt: Metrics summary (e.g., total logs, error rates).

reports/structured_report.csv: Structured CSV report.

reports/structured_report.json: Structured JSON report.

reports/realtime_metrics.json: Continuously updated real-time metrics.

Example CSV Output (reports/output.csv):

text
Copy code
Timestamp,Level,Message
2025-09-04 19:00,INFO,User login successful
2025-09-04 19:05,ERROR,Failed password attempt
2025-09-04 19:10,WARNING,Disk usage 90%
📉 Visualizations
Automatically saved in reports/plots/ with timestamps:

logs_by_level_<timestamp>.png: Bar chart of logs by level (INFO, ERROR, WARNING).

error_rate_<timestamp>.png: Pie chart of error vs non-error logs.

📊 Interactive Dashboard
Launch the Dash/Streamlit dashboard to monitor logs in real-time, view live metrics, and explore visualizations.

🔍 Advanced Features
Real-Time Ingestion: Processes logs as they arrive using a lightweight Python queue.

Anomaly Detection: ML-powered identification of unusual log patterns.

Log Correlation: Correlates logs from multiple sources for deeper insights.

Interactive Dashboard: Visualize trends, errors, and metrics in real-time.

🛠️ Contributing
Fork the repository.

Create a new branch:

bash
Copy code
git checkout -b feature/your-feature
Commit your changes:

bash
Copy code
git commit -m "Add your feature"
Push to the branch:

bash
Copy code
git push origin feature/your-feature
Open a Pull Request.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

💻 Built with love for SOC teams to stay one step ahead of threats!

yaml
Copy code

---

Do you also want me to **add emoji icons** (📦, 📝, 📊) before *each subheading* like in your screenshot for more style
