from dash import callback, Input, Output
import plotly.express as px
from utils.load_data import driver_yearly, total_driver_points

@callback(
    Output('driver-performance-plot', 'figure'),
    Input('driver-selector', 'value'),
    Input('top-n-driver-slider', 'value')
)
def update_driver_plot(selected_drivers, top_n):
    if selected_drivers:
        filtered = driver_yearly[driver_yearly['driver_name'].isin(selected_drivers)]
    else:
        top_names = total_driver_points.head(top_n)["driver_name"].tolist()
        filtered = driver_yearly[driver_yearly['driver_name'].isin(top_names)]

    return px.line(
        filtered,
        x="year",
        y="points",
        color="driver_name",
        markers=True,
        title="Driver Points per Season"
    )
