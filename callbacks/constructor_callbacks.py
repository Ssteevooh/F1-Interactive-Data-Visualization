from dash import callback, Input, Output
import plotly.express as px
from utils.load_data import constructor_yearly, total_constructor_points

@callback(
    Output('constructor-performance-plot', 'figure'),
    Input('constructor-selector', 'value'),
    Input('top-n-constructor-slider', 'value')
)
def update_constructor_plot(selected_constructors, top_n):
    if selected_constructors:
        filtered = constructor_yearly[constructor_yearly["constructor_name"].isin(selected_constructors)]
    else:
        top_names = total_constructor_points.head(top_n)["constructor_name"].tolist()
        filtered = constructor_yearly[constructor_yearly["constructor_name"].isin(top_names)]

    return px.line(
        filtered,
        x="year",
        y="points",
        color="constructor_name",
        markers=True,
        title="Constructor Points per Season"
    )
