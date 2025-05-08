from dash import callback, Input, Output
import plotly.express as px
from utils.load_data import grid_data

callback(
    Output('grid-vs-position-plot', 'figure'),
    Input('grid-driver-selector', 'value')
)
def update_grid_plot(selected_names):
    if selected_names:
        filtered = grid_data[grid_data["driver_name"].isin(selected_names)]
    else:
        filtered = grid_data.copy()

    plot_data = filtered.sample(n=min(1000, len(filtered)), random_state=42)

    fig = px.scatter(
        plot_data,
        x="grid",
        y="position",
        color="driver_name",
        hover_data=["name_x", "year"],
        title="Grid vs Final Position"
    )
    fig.update_yaxes(autorange="reversed")
    return fig
