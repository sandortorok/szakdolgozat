from dash import html, Input,Output, dcc
import dash_defer_js_import as dji
import dash

class energy:
    def __init__(self, app):
        self.layout = html.Div([
            self.createInterval(),
            html.Canvas(id = 'c'),
            html.H1("CURRENT CONSUMPTION", className="unselectable", style={'textAlign': "center",'marginTop' : '15%'}),
            html.H2("20 kWh", className="unselectable", id = "e_val", style={'textAlign': "center", 'color' : 'white'}),
            html.Article(dji.Import(src='/assets/lightning.js'))
        ])
        self.app = app
        self.energychange_callback()

    def createInterval(self):
        interval = dcc.Interval(
            id = "interval-component",
            interval=100, # in milliseconds
            n_intervals=0,

        )
        return interval

    def callback(self, value):
        return "{} kWh".format(value)

    def energychange_callback(self):
        self.app.callback(dash.dependencies.Output('e_val', 'children'),
                    [dash.dependencies.Input('interval-component', 'n_intervals')]
        )(self.callback)

