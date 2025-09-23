import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load CSV data (real sales over time)
df_csv = pd.read_csv("smoothie_sales.csv", parse_dates=["Date"])

# Sample hardcoded data (sales by day for demo)
df_static = pd.DataFrame({
    "Smoothie": ["Banana", "Mango", "Berry", "Papaya", "Mango", "Banana"],
    "Sales": [150, 200, 180, 90, 220, 170],
    "Day": ["Mon", "Mon", "Mon", "Mon", "Tue", "Tue"]
})

# Initialize Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("🍹 Data Delights - Smoothie Dashboard", style={'textAlign': 'center'}),

    html.H2("📅 CSV-based Sales Over Time", style={'marginTop': '30px'}),
    dcc.Dropdown(
        id='csv-smoothie-filter',
        options=[{'label': smoothie, 'value': smoothie} for smoothie in df_csv['Smoothie'].unique()],
        value='Mango'
    ),
    dcc.Graph(id='csv-sales-over-time'),

    html.Br(),

    dcc.Graph(
        id='csv-total-sales-bar',
        figure=px.bar(
            df_csv.groupby("Smoothie").sum(numeric_only=True).reset_index(),
            x="Smoothie", y="Sales", color="Smoothie", title="Total Sales by Smoothie (CSV)"
        )
    ),

    html.H2("📊 Static Smoothie Sales by Day (Sample Data)", style={'marginTop': '30px'}),
    dcc.Dropdown(
        id='static-smoothie-dropdown',
        options=[{'label': s, 'value': s} for s in df_static['Smoothie'].unique()],
        value='Mango'
    ),
    dcc.Graph(id='static-sales-graph')
])

# Callback for CSV-based line chart
@app.callback(
    Output('csv-sales-over-time', 'figure'),
    Input('csv-smoothie-filter', 'value')
)
def update_csv_time_series(selected_smoothie):
    filtered_df = df_csv[df_csv['Smoothie'] == selected_smoothie]
    fig = px.line(filtered_df, x="Date", y="Sales", title=f"{selected_smoothie} Sales Over Time (CSV)")
    return fig

# Callback for static bar chart
@app.callback(
    Output('static-sales-graph', 'figure'),
    Input('static-smoothie-dropdown', 'value')
)
def update_static_graph(selected_smoothie):
    filtered = df_static[df_static['Smoothie'] == selected_smoothie]
    fig = px.bar(filtered, x="Day", y="Sales", title=f"{selected_smoothie} Sales by Day (Sample Data)")
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
