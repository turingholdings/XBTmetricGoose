import dash
from dash import dcc, html
import pandas as pd
from datetime import datetime, timedelta
import random

# === Generate Mock 90-Day MVRV Z-Score Data ===
def get_mock_mvrv_data():
    today = datetime.today()
    dates = [today - timedelta(days=i) for i in range(89, -1, -1)]  # 90 days
    scores = [round(random.uniform(1.5, 3.5), 2) for _ in range(90)]
    df = pd.DataFrame({'timestamp': dates, 'value': scores})
    current_value = df.iloc[-1]['value']
    return df, current_value

# === Build Dash App ===
app = dash.Dash(__name__)
app.title = "MVRV Z-Score"

# Use mock data
mvrv_df, current_score = get_mock_mvrv_data()

# === Layout ===
app.layout = html.Div(
    style={"backgroundColor": "white", "padding": "20px"},
    children=[
        html.H1("MVRV Z-Score", style={"textAlign": "center"}),
        html.H2(f"Current Value: {current_score}", style={"textAlign": "center", "color": "darkblue"}),
        dcc.Graph(
            figure={
                "data": [{
                    "x": mvrv_df["timestamp"],
                    "y": mvrv_df["value"],
                    "type": "line",
                    "name": "MVRV Z-Score"
                }],
                "layout": {
                    "title": "Last 90 Days of MVRV Z-Score",
                    "xaxis": {"title": "Date"},
                    "yaxis": {"title": "Z-Score"},
                    "plot_bgcolor": "white",
                    "paper_bgcolor": "white"
                }
            }
        )
    ]
)

# === Run Locally ===
if __name__ == "__main__":
    app.run(debug=True)

# For Render deployment
server = app.server
