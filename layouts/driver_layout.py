from dash import html, dcc
from utils.load_data import total_driver_points

driver_layout = html.Div([
    html.H2("Driver Performance Over Time"),
    html.Label("Search or Select Driver(s):"),
    dcc.Dropdown(
        id='driver-selector',
        options=[{"label": name, "value": name} for name in total_driver_points["driver_name"].unique()],
        multi=True,
        placeholder="Select driver(s)..."
    ),
    dcc.Slider(
        id='top-n-driver-slider',
        min=5, max=20, step=5, value=10,
        marks={i: f"Top {i}" for i in [5, 10, 15, 20]}
    ),
    dcc.Graph(
        id='driver-performance-plot',
        className="graph"
        )
])
