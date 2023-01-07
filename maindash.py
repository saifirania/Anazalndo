import dash
import dash_bootstrap_components as dbc

dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css")
external_stylesheets = dbc.themes.BOOTSTRAP

app = dash.Dash(__name__,
 external_stylesheets=[external_stylesheets, dbc_css],
 assets_folder= "assets",
 title= "AnalyserZalando",
 suppress_callback_exceptions=True
 )

