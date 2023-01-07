from dash import dcc,html
import dash_bootstrap_components as dbc
from dash import Input, Output,  html,State
from maindash import app


import time

from assets.additional_css import containerStyle
from assets.additional_css import TabContainerStyle
from assets.additional_css import tab_style
from assets.additional_css import tab_selected_style


from views.price_best import price_best
from views.price_cheap import price_cheap
from views.price_average import price_average
from views.price_expensive import price_expensive

from views.brand import make_marque









def make_taps():
    return   html.Div(
                        [                        
                            dbc.Container(
                                style= containerStyle,
                                children=[
                                dcc.Tabs(
                                        id="tabs-example-graph", 
                                        value='tab-1-example-graph',
                                        style=  TabContainerStyle,
                                        vertical= True,
                                        children=[

                                                
                                                    dcc.Tab(
                                                                label='Find your best Brand', 
                                                                style=tab_style, 
                                                                selected_style=tab_selected_style,
                                                                children=[
                                                                    dbc.Container(
                                                                        style = {
                                                                            "width":"1000px",
                                                                            'height': '1200px',
                                                                            'padding': '25px',

                                                                        },
                                                                        children=[
                                                                            make_marque()

                                                                        ]
                                                                        ),
                                                                                
                                                                            
                                                                                ]
                                                            ),
                                                            
                                                    dcc.Tab(
                                                                label='Best recommanded products',
                                                                style=tab_style, 
                                                                selected_style=tab_selected_style,
                                                                children=[
                                                                    dbc.Container(
                                                                        style = {
                                                                            "width":"1000px",
                                                                            'height': '1200px',
                                                                            'padding': '25px',

                                                                        },
                                                                        children=[
                                                                               price_best()
                                                                         ]
                                                                        ),
                                                                                
                                                                            
                                                                        ]
                                                            ),


                                                    dcc.Tab(
                                                                label='Cheapest products',
                                                                style=tab_style, 
                                                                selected_style=tab_selected_style,
                                                                children=[
                                                                    dbc.Container(
                                                                        style = {
                                                                            "width":"1000px",
                                                                            'height': '1200px',
                                                                            'padding': '25px',

                                                                        },
                                                                        children=[
                                                                               price_cheap()
                                                                         ]
                                                                        ),
                                                                                
                                                                            
                                                                        ]
                                                            ),


                                                    dcc.Tab(
                                                                label='Average price products',
                                                                style=tab_style, 
                                                                selected_style=tab_selected_style,
                                                                children=[
                                                                    dbc.Container(
                                                                        style = {
                                                                            "width":"1000px",
                                                                            'height': '1200px',
                                                                            'padding': '25px',

                                                                        },
                                                                        children=[
                                                                               price_average()
                                                                         ]
                                                                        ),
                                                                                
                                                                            
                                                                        ]
                                                            ),

                                                    dcc.Tab(
                                                                label='Top expensive products',
                                                                style=tab_style, 
                                                                selected_style=tab_selected_style,
                                                                children=[
                                                                    dbc.Container(
                                                                        style = {
                                                                            "width":"1000px",
                                                                            'height': '1200px',
                                                                            'padding': '25px',

                                                                        },
                                                                        children=[
                                                                               price_expensive()
                                                                         ]
                                                                        ),
                                                                                
                                                                            
                                                                        ]
                                                            ),                                                                                                                      


                                                
                                                            
                                                  


                                                
                                                
                                                ]
                                        ),
                                    
                                ]
                                    ),
                    

                        ])
    

