import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# Load and prepare data
df = pd.read_csv("data/formatted_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Build the app
app = Dash(__name__)

app.layout = html.Div(
    className="app-container",
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            className="app-header",
        ),
        html.P(
            "Explore how Pink Morsel sales changed over time, "
            "before and after the price increase on 15 January 2021.",
            className="app-subheader",
        ),
        html.Div(
            className="filter-container",
            children=[
                html.Label("Filter by region:", className="filter-label"),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                        {"label": "All", "value": "all"},
                    ],
                    value="all",
                    className="region-radio",
                    inline=True,
                ),
            ],
        ),
        dcc.Graph(id="sales-line-chart", className="chart"),
    ],
)


@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value"),
)
def update_chart(selected_region):
    # Filter by region if needed
    if selected_region == "all":
        filtered = df
    else:
        filtered = df[df["region"] == selected_region]

    # Aggregate daily sales (sums across regions when "all" is selected)
    daily = filtered.groupby("date", as_index=False)["sales"].sum()

    fig = px.line(
        daily,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales — {selected_region.capitalize()} region",
        labels={"date": "Date", "sales": "Sales ($)"},
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        hovermode="x unified",
        title_x=0.5,
    )
    fig.update_xaxes(showgrid=True, gridcolor="#eee")
    fig.update_yaxes(showgrid=True, gridcolor="#eee")

    return fig


if __name__ == "__main__":
    app.run(debug=True)
