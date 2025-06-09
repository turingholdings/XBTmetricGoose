<<<<<<< HEAD
#!/usr/bin/env python
# coding: utf-8

# In[11]:


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


# In[ ]:




=======
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "3c16b055-e677-4ea6-9c40-ac42982fd739",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x1480ab9e0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import dash\n",
    "from dash import dcc, html\n",
    "import pandas as pd\n",
    "from datetime import datetime, timedelta\n",
    "import random\n",
    "\n",
    "# === Generate Mock 30-Day MVRV Z-Score Data ===\n",
    "def get_mock_mvrv_data():\n",
    "    today = datetime.today()\n",
    "    dates = [today - timedelta(days=i) for i in range(29, -1, -1)]\n",
    "    scores = [round(random.uniform(1.5, 3.5), 2) for _ in range(30)]\n",
    "    df = pd.DataFrame({'timestamp': dates, 'value': scores})\n",
    "    current_value = df.iloc[-1]['value']\n",
    "    return df, current_value\n",
    "\n",
    "# === Build Dash App ===\n",
    "app = dash.Dash(__name__)\n",
    "app.title = \"MVRV Z-Score\"\n",
    "\n",
    "# Use mock data\n",
    "mvrv_df, current_score = get_mock_mvrv_data()\n",
    "\n",
    "# === Layout ===\n",
    "app.layout = html.Div([\n",
    "    html.H1(\"MVRV Z-Score\", style={\"textAlign\": \"center\"}),\n",
    "    html.H2(f\"Current Value: {current_score}\", style={\"textAlign\": \"center\", \"color\": \"darkblue\"}),\n",
    "    dcc.Graph(\n",
    "        figure={\n",
    "            \"data\": [{\n",
    "                \"x\": mvrv_df[\"timestamp\"],\n",
    "                \"y\": mvrv_df[\"value\"],\n",
    "                \"type\": \"line\",\n",
    "                \"name\": \"MVRV Z-Score\"\n",
    "            }],\n",
    "            \"layout\": {\n",
    "                \"title\": \"Last 30 Days of MVRV Z-Score\",\n",
    "                \"xaxis\": {\"title\": \"Date\"},\n",
    "                \"yaxis\": {\"title\": \"Z-Score\"},\n",
    "            }\n",
    "        }\n",
    "    )\n",
    "])\n",
    "\n",
    "# === Run Locally ===\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "5c9624e5-33e1-4770-8958-affde6e160ea",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
>>>>>>> 2381c66cc19d825b126da9b28c5bccbb52a34f0c
