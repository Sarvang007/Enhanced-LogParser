Enhanced Log Parser

A Python-based log parsing and reporting tool designed for SOC (Security Operations Center) workflows.
This tool helps analyze log files (e.g., syslogs, Windows event logs, custom app logs) and outputs structured data for further analysis.


📂 Project Structure
enhanced-log-parser/
│
├── src/               # Core source code
│   ├── __init__.py
│   ├── main.py        # Entry point of the project
│   ├── parser.py      # Log parsing logic
│   ├── utils.py       # Utility functions
│
├── tests/             # Unit tests
│   ├── __init__.py
│   ├── test_parser.py
│
├── reports/           # Generated reports (CSV/JSON/etc.)
├── logs/              # Sample log files for testing
│   └── sample.log
│
├── .gitignore         # Ignored files (venv, __pycache__, etc.)
├── requirements.txt   # Dependencies
├── README.md          # Project documentation


Phase 1 Progress
Phase	    Step	    Task	                                                        Status
Phase 1	    Step 1	    Setup virtual environment & install requirements	            ✅ Completed
Phase 1	    Step 2	    Create project structure (folders & files)	                    ✅ Completed
Phase 1	    Step 3	    Initialize Git & commit skeleton	                            ✅ Completed
Phase 1	    Step 4	    Implement basic log parser (reads sample.log, extracts fields)	✅ Completed
Phase 1	    Step 5	    Add unit test for parser	                                    ✅ Completed
Phase 1	    Step 6	    Generate first report (CSV/JSON output)	                        ✅ Completed


⚙️ Setup Instructions


1. Clone the repository
git clone https://github.com/yourusername/enhanced-log-parser.git
cd enhanced-log-parser

2. Setup virtual environment
python -m venv .venv
.venv\Scripts\activate   # On Windows
source .venv/bin/activate # On Linux/Mac

3. Install dependencies
pip install -r requirements.txt

▶️ Usage
Run the parser:
python -m src.main

Sample log format (logs/sample.log):
2025-09-04 19:00 INFO User login successful
2025-09-04 19:05 ERROR Failed password attempt
2025-09-04 19:10 WARNING Disk usage 90%

📊 Output
Parsed logs are saved in:
reports/output.csv

Example CSV output:

Timestamp	        Level	    Message
2025-09-04 19:00	INFO	    User login successful
2025-09-04 19:05	ERROR	    Failed password attempt
2025-09-04 19:10	WARNING	    Disk usage 90%


Updated-Project Structure for Phase-2
enhanced-log-parser/
│
├── src/               # Core source code
│   ├── __init__.py
│   ├── main.py        # Entry point of the project
│   ├── parser.py      # Log parsing logic
│   ├── metrics.py     # Metrics calculation + report saving
│   ├── visualize.py   # Visualization (charts & plots)
│   ├── utils.py       # Utility functions
│
├── tests/             # Unit tests
│   ├── __init__.py
│   ├── test_parser.py
│
├── reports/           # Generated reports (CSV/JSON/plots)
│   ├── output.csv
│   ├── summary.txt
│   ├── structured_report.csv
│   ├── structured_report.json
│   └── plots/
│       ├── logs_by_level_<timestamp>.png
│       └── error_rate_<timestamp>.png
│
├── logs/              # Sample log files for testing
│   └── sample.log
│
├── .gitignore         # Ignored files (venv, __pycache__, etc.)
├── requirements.txt   # Dependencies
├── README.md          # Project documentation


✅ Phase 2 Progress

Phase	    Step	    Task	                                                                Status
Phase 2	    Step 1	    Implement metrics calculation (total logs, error rates, top IPs)	    ✅ Completed
Phase 2	    Step 2	    Generate summary report (text output)	                                ✅ Completed
Phase 2	    Step 3	    Generate CSV/JSON structured report	                                    ✅ Completed
Phase 2	    Step 4	    Implement static visualizations (counts, error trends, top IPs etc.)	✅ Completed
Phase 2	    Step 5	    Save plots automatically in reports/plots/	                            ✅ Completed


📈 Outputs

Reports
reports/output.csv - raw parsed logs
reports/summary.txt - metrics summary
reports/structured_report.csv - structured CSV with logs
reports/structured_report.json - structured JSON report


Visualizations
Automatically saved with timestamps in reports/plots/:
logs_by_level_<timestamp>.png - Bar chart of logs per level
error_rate_<timestamp>.png - Pie chart of error vs non-error logs


Updated-Project Structure for Phase-3
enhanced-log-parser/
│
├── src/                    
│   ├── __init__.py
│   ├── main.py              # Batch log parsing
│   ├── parser.py            # Log parsing logic
│   ├── metrics.py           # Metrics + summary/structured reports
│   ├── visualize.py         # Static plots
│   ├── realtime_ingestion.py # Real-time ingestion with threading + queue
│   ├── dashboard.py         # Dash live dashboard (charts + log feed)
│   ├── anomaly_detection.py # ML anomaly detection
│   ├── correlation.py       # Correlation engine (Phase 3 Step 5)
│   ├── utils.py             # Utility functions
│
├── tests/                  
│   ├── __init__.py
│   ├── test_parser.py
│
├── reports/                
│   ├── output.csv
│   ├── summary.txt
│   ├── structured_report.csv
│   ├── structured_report.json
│   ├── realtime_metrics.json   # Continuously updated
│   └── plots/                 
│       ├── logs_by_level_<timestamp>.png
│       └── error_rate_<timestamp>.png
│
├── logs/                    
│   └── sample.log
│
├── requirements.txt         
├── README.md                


🚀 Phase 3 Progress

Phase	    Step	    Task	                                            	    Status	    
Phase 3	    Step 1	    Real-Time Ingestion(Lightweight Python Queue)               ✅ Completed	   
Phase 3	    Step 2	    Stream Processing(Aggregation in Real-Time)	                ✅ Completed	
Phase 3	    Step 3	    Interactive Dashboard(Dash/Streamlit)	                    ✅ Completed	
Phase 3	    Step 4	    Machine Learning Parsing(Anomaly Detection)	        	    ✅ Completed	
Phase 3	    Step 5	    Log Correlation Engine(Multi-source correlation)            ✅ Completed	