import time
from dash import dcc,html
import dash_bootstrap_components as dbc
from dash import Input, Output,  html,State
from maindash import app


from views.haider import Mainnavbar
from views.mainwebsite import MainWebsite




def make_layout():
    return html.Div([
                    Mainnavbar,
                    MainWebsite
                    ]
                    
                    )




