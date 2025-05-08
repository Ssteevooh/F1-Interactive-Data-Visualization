from dash import html, dcc
import plotly.express as px
from utils.load_data import circuits_df

fig = px.scatter_geo(
    circuits_df,
    lat="lat",
    lon="lng",
    hover_name="name",
    hover_data=["location", "country"],
    projection="natural earth",
    title="F1 Circuits Around the World"
)

map_layout = html.Div([
    html.H2("F1 Circuits Map"),
    dcc.Graph(
        figure=fig, 
        className="graph"
        )
])
