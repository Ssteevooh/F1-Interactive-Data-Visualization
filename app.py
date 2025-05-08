from dash import html, dcc
from server import app

from layouts.driver_layout import driver_layout
from layouts.constructor_layout import constructor_layout
from layouts.grid_layout import grid_layout
from layouts.map_layout import map_layout

import callbacks.driver_callbacks
import callbacks.constructor_callbacks
import callbacks.grid_callbacks

app.layout = html.Div([
    html.H1("F1 Performance Dashboard"),
    dcc.Tabs([
        dcc.Tab(label="🏎 Driver Performance", children=[driver_layout]),
        dcc.Tab(label="🏁 Constructor Performance", children=[constructor_layout]),
        dcc.Tab(label="📉 Start vs Finish Positions", children=[grid_layout]),
        dcc.Tab(label="🌍 Circuits Map", children=[map_layout]),

    ])
])

if __name__ == "__main__":
    app.run(debug=True)
