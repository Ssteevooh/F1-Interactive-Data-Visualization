from dash import html, dcc
from utils.load_data import all_driver_names

grid_layout = html.Div([
    html.H2("Grid Position vs Final Position"),
    html.Label("Select Driver(s):"),
    dcc.Dropdown(
        id='grid-driver-selector',
        options=[{"label": name, "value": name} for name in all_driver_names],
        multi=True,
        placeholder="Search or select driver(s)..."
    ),
    dcc.Graph(id='grid-vs-position-plot',
              className="graph"
              )
])
