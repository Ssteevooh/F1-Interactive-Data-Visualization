""""

from dash import Output
import plotly.express as px
from server import app
from utils.load_data import circuits_df

@app.callback(
    Output("circuit-map", "figure"),
    [],
    []
)
def display_circuit_map():
    fig = px.scatter_geo(
        circuits_df,
        lat="lat",
        lon="lng",
        hover_name="name",
        hover_data=["location", "country"],
        projection="natural earth",
        title="F1 Circuits (Geographic View)"
    )
    return fig
"""