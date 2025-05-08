from dash import Dash, html

app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "F1 Interactive Dashboard"

server = app.server
