import dash_bootstrap_components as dbc
import dash
from dash import html
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Carousel(
    items=[
        {"key": "1", "src": "/assets/back1.jpg", "img_style" : {'height':'100vh'}, "header" : "SLIDE 1"},
        {"key": "2", "src": "/assets/back1.jpg", "img_style" : {'height':'100vh'}, "header" : "THIS IS SLIDE 2"},
        {"key": "3", "src": "/assets/back1.jpg", "img_style" : {'height':'100vh'}, "header" : "LETS GOOOOOOOOOOOO"},
    ],
    controls=True,
    indicators=True,
    className="carousel-fade",
)





if __name__ == '__main__':
    app.run_server(debug=False)
