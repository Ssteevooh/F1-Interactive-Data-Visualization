from dash import html, dcc
from utils.load_data import total_constructor_points

constructor_layout = html.Div([
    html.H2("Constructor Performance Over Time"),
    html.Label("Search or Select Constructor(s):"),
    dcc.Dropdown(
        id='constructor-selector',
        options=[{"label": name, "value": name} for name in total_constructor_points["constructor_name"].unique()],
        multi=True,
        placeholder="Select constructor(s)..."
    ),
    dcc.Slider(
        id='top-n-constructor-slider',
        min=5, max=20, step=5, value=10,
        marks={i: f"Top {i}" for i in [5, 10, 15, 20]}
    ),
    dcc.Graph(
        id='constructor-performance-plot', 
        className="graph"
        ),
])
