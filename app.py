import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# Load the formatted data produced by data_processing.py
df = pd.read_csv("data/formatted_sales_data.csv")

# Sort by date so the line chart draws in chronological order
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# For the main chart, aggregate sales across regions per day
daily_sales = df.groupby("date", as_index=False)["sales"].sum()

# Build the line chart
fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Sales ($)"},
)

price_increase_date = pd.to_datetime("2021-01-15")

fig.add_vline(
    x=price_increase_date.timestamp() * 1000,
    line_dash="dash",
    line_color="red",
    annotation_text="Price increase (15 Jan 2021)",
    annotation_position="top right",
)

# Build the app
app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            style={"textAlign": "center"},
        ),
        html.P(
            "Daily sales of Pink Morsels across all regions.",
            style={"textAlign": "center"},
        ),
        dcc.Graph(id="sales-line-chart", figure=fig),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
