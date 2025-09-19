import json
import os
from dash import Dash, dcc, html, dash_table
import plotly.express as px
from dash.dependencies import Input, Output

# Path to metrics file
METRICS_FILE = os.path.join(os.path.dirname(__file__), "..", "reports", "realtime_metrics.json")

# Initialize Dash app
app = Dash(__name__)
app.title = "SOC Log Dashboard"

# Layout
app.layout = html.Div([
    html.H1("📊 Real-Time Log Monitoring Dashboard", style={"textAlign": "center"}),

    html.Div(id="total-logs", style={"fontSize": "20px", "marginBottom": "20px"}),

    dcc.Graph(id="level-bar"),
    dcc.Graph(id="error-pie"),

    html.H3("📜 Live Log Feed"),
    dash_table.DataTable(
        id="log-feed",
        columns=[
            {"name": "Timestamp", "id": "timestamp"},
            {"name": "Level", "id": "level"},
            {"name": "Message", "id": "message"},
        ],
        style_cell={"textAlign": "left", "padding": "5px", "fontFamily": "monospace"},
        style_header={"backgroundColor": "#f4f4f4", "fontWeight": "bold"},
        style_table={"height": "300px", "overflowY": "auto"},
        style_data_conditional=[
            {   # 🔴 ERROR logs in red
                "if": {"filter_query": "{level} = 'ERROR'"},
                "backgroundColor": "#ffcccc",
                "color": "red",
                "fontWeight": "bold"
            },
            {   # 🟡 WARNING logs in yellow
                "if": {"filter_query": "{level} = 'WARNING'"},
                "backgroundColor": "#fff3cd",
                "color": "#856404",
                "fontWeight": "bold"
            },
            {   # 🟢 INFO logs in green
                "if": {"filter_query": "{level} = 'INFO'"},
                "backgroundColor": "#d4edda",
                "color": "#155724",
            },
        ],
    ),

    html.H3("🚨 Correlation Alerts"),
    dash_table.DataTable(
        id="alerts-feed",
        columns=[{"name": "Alert", "id": "alert"}],
        style_cell={"textAlign": "left", "padding": "5px", "fontFamily": "monospace"},
        style_header={"backgroundColor": "#f8d7da", "fontWeight": "bold", "color": "darkred"},
        style_table={"height": "200px", "overflowY": "auto"},
        style_data={"color": "darkred", "fontWeight": "bold"}
    ),

    # Refresh interval (every 3 seconds)
    dcc.Interval(
        id="interval-component",
        interval=3*1000,
        n_intervals=0
    )
])

@app.callback(
    [Output("total-logs", "children"),
     Output("level-bar", "figure"),
     Output("error-pie", "figure"),
     Output("log-feed", "data"),
     Output("alerts-feed", "data")],
    [Input("interval-component", "n_intervals")]
)
def update_dashboard(n):
    if not os.path.exists(METRICS_FILE):
        return "⚠️ No metrics file found.", px.scatter(), px.pie(values=[1], names=["No Data"]), [], []

    try:
        with open(METRICS_FILE, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        return "⚠️ Error reading metrics file.", px.scatter(), px.pie(values=[1], names=["Bad Data"]), [], []

    # ✅ Metrics
    total_logs = data.get("total_logs", 0)
    level_counts = data.get("level_counts", {})
    error_rate = data.get("error_rate", 0)

    # ✅ Logs (last 20 only)
    logs = data.get("logs", [])
    log_feed_data = [
        {"timestamp": log[0], "level": log[1], "message": log[2]}
        for log in logs[-20:]
    ]

    # ✅ Correlation Alerts
    alerts = data.get("alerts", [])
    alerts_data = [{"alert": alert} for alert in alerts[-10:]]  # show last 10 alerts

    # Bar chart
    if not level_counts:
        fig_bar = px.bar(x=["No Data"], y=[0], title="Logs by Level")
    else:
        fig_bar = px.bar(
            x=list(level_counts.keys()),
            y=list(level_counts.values()),
            labels={"x": "Log Level", "y": "Count"},
            title="Logs by Level",
            color=list(level_counts.keys())
        )

    # Pie chart
    fig_pie = px.pie(
        values=[error_rate, max(0, 100 - error_rate)],
        names=["Error Logs", "Other Logs"],
        title="Error Rate Distribution"
    )

    return f"✅ Total Logs: {total_logs}", fig_bar, fig_pie, log_feed_data, alerts_data


if __name__ == "__main__":
    app.run(debug=True)
