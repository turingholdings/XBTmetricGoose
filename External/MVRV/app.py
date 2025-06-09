import dash
from dash import dcc, html
import pandas as pd
from datetime import datetime, timedelta
import random

# === Generate Mock 30-Day MVRV Z-Score Data ===
def get_mock_mvrv_data():
    today = datetime.today()
    dates = [today - timedelta(days=i) for i in range(29, -1, -1)]
    scores = [round(random.uniform(1.5, 3.5), 2) for _ in range(30)]
    df = pd.DataFrame({'timestamp': dates, 'value': scores})
    current_value = df.iloc[-1]['value']
    return df, current_value

# === Build Dash App ===
app = dash.Dash(__name__)
server = app.server  # <-- this is the important line for gunicorn

app.title = "MVRV Z-Score"

# Use mock data
mvrv_df, current_score = get_mock_mvrv_data()

# === Layout ===
app.layout = html.Div([
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
                "title": "Last 30 Days of MVRV Z-Score",
                "xaxis": {"title": "Date"},
                "yaxis": {"title": "Z-Score"},
            }
        }
    )
])

# === Run Locally ===
if __name__ == "__main__":
    app.run(debug=True)
server = app.server  # Expose the Dash server to Gunicorn

