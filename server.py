from dash import Dash, html

app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "F1 Interactive Dashboard"

app.layout = html.Div([
    html.H1("F1 Interactive Dashboard is running!")
])

server = app.server
