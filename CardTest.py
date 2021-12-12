from os import path
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html, dcc
import dash
from dash_bootstrap_components._components.Container import Container
import dash_defer_js_import as dji
import energy_card_layout as ecl
from humidity_card_layout import h_layout
def createNavbar():
    search_bar = dbc.Row(
        [
            dbc.Col(dbc.Input(type="search", placeholder="Search")),
            dbc.Col(
                dbc.Button(
                    "Search", color="primary", className="ms-2", n_clicks=0
                ),
                width="auto",
            ),
        ],
        className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
        align="center",
    )

    navbar = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src="/assets/iot.png", height="40px")),
                            dbc.Col(dbc.NavbarBrand("Sensor Selector", className="ms-2")),
                        ],
                        className="g-0",
                    ),
                    href="/",
                    style={"textDecoration": "none"},
                ),
                dbc.Collapse(
                    search_bar,
                    id="navbar-collapse",
                    is_open=False,
                    navbar=True,
                ),
            ]
        ),
        color="dark",
        dark=True,
    )
    return navbar

def createCard(src, name, description, buttonname, ref):   
    card = dbc.Card(
    [
        dbc.CardImg(src="/assets/{}".format(src), style = {"height" : "10rem"}),
        dbc.CardBody(
            [
                html.H4("{}".format(name), className="card-title"),
                html.P(
                    """{}, KATTINTS A GOMBRA TÖBB INFÓÉRT """.format(description),
                    className="card-text",
                ),
                dbc.Button("{}".format(buttonname), color="info", href=ref),
            ]
        ),
    ],
    style={"width": "18rem"}, outline= True)
    return card

def createRows():
    rowarray = []
    card1 = createCard("waterlevel.jpg", "VÍZSZINT", "A JELENLEGI VÍZSZINT 103 MÉTER", "WATERLEVEL", "/waterlevel")
    card2 = createCard("water.jpeg", "VÍMENNYISÉG", "A JELENLEGI VÍZMENNYISÉG 1 LITER", "WATER", "/water")
    card3 = createCard("ammonia.jpg", "AMMÓNIA", "A JELENLEGI AMMÓNIA SZINT 10 PPM", "AMMONIA", "/ammonia")
    card4 = createCard("temperature.jpg", "HŐMÉRSÉKLET", "A JELENLEGI HŐMÉRSÉKLET 20 °C", "TEMPERATURE", "/temperature")
    card5 = createCard("pressure.jpg", "LÉGNYOMÁS", "A JELENLEGI LÉGNYOMÁS 101 kPA", "AIR PRESSURE", "/pressure")
    card6 = createCard("humidity.png", "PÁRATARTALOM", "A JELENLEGI PÁRATARTALOM 45%", "HUMIDITY", "/humidity")
    card7 = createCard("energy.jpg", "ÁRAMFOGYASZTÁS", "A JELENLEGI ÁRAMFOGYASZTÁS 120 kWh", "ENERGY", "/energy")

    row1 = dbc.Row(
        [
            dbc.Col(card1, width = 2),
            dbc.Col(card2, width= 2),
            dbc.Col(card3, width= 2),
            dbc.Col(card4, width= 2),
            dbc.Col(card5, width= 2),
            dbc.Col(card6, width= 2),
        ],
        className="m-4",
    )
    rowarray.append(row1)
    row2 = dbc.Row(
        [
            dbc.Col(card7, width = 2),
            # dbc.Col(card2, width= 2),
            # dbc.Col(card3, width= 2),
            # dbc.Col(card4, width= 2),
            # dbc.Col(card5, width= 2),
            # dbc.Col(card6, width= 2),
        ],
        className="m-4",
    )
    rowarray.append(row2)
    return rowarray


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], suppress_callback_exceptions=True)
energy = ecl.energy(app)
app.layout = html.Div([
    createNavbar(),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

main_layout = html.Div([
    createRows()[0], createRows()[1]
])
waterlevel_layout = html.Div([
    html.Div(className = "cup"),
    html.H1('WATERLEVEL PAGE'),
])
water_layout = html.Div([
    html.Div(className = "cup"),
    html.H1('WATER PAGE'),
])
ammonia_layout = html.Div([
    html.H1('AMMONIA PAGE'),
])
temperature_layout = html.Div([
    html.Div(className = "thermometer"),
    html.H2('TEMPERATURE PAGE'),
])
pressure_layout = html.Div([
    html.H1('AIR PRESSURE PAGE'),
])



@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/waterlevel':
        return waterlevel_layout
    elif pathname == '/water':
        return water_layout
    elif pathname == '/ammonia':
        return ammonia_layout
    elif pathname == '/temperature':
        return temperature_layout
    elif pathname == '/pressure':
        return pressure_layout
    elif pathname == '/humidity':
        return h_layout
    elif pathname == '/energy':
        return energy.layout
    else:
        return main_layout
    # You could also return a 404 "URL not found" page here




if __name__ == '__main__':
    app.run_server(debug=True)
