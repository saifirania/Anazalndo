import dash_bootstrap_components as dbc
from dash import html 







def make_product_card(title,description,sexe,mark,url_pic,finalp,originp,promo):
    
    return  html.Div([
    dbc.Container(
        style = {
            "width":"1000px",
            'height': '500px',
            'padding': '15px',
            'margin':'20px'

        },
        children=[                      
                    dbc.Card(
                        color="#2f323a",

                        children=[

                            dbc.CardHeader(
                                title,
                                style = {  
                                            'color': '#2f323a',
                                            'justify': 'center',
                                            "background-color":"#4ECDC4",
                                            'align': 'center',
                                            'fontWeight': 'bold',
                                            "margin":"5px 0px 5px 0px",
                                            "fontFamily": "Roboto",
                                            "display": "block",
                                            'fontSize':"30px",
                                            'padding': '15px',
                                            'margin':'30px'                                           

                                        }
                                ),
                            
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.CardImg(
                                            src= url_pic,
                                            style = {
                                                "height":"150", 
                                                "width":"400",
                                                'maxHeight': '100%',
                                                'padding': '15px',
                                                'margin':'20px' 
                                                },
                                            top = False,
                                            className="img-fluid rounded-start",
                                        ),
                                        className="col-md-4",
                                            ),

                                    dbc.Col(
                                        dbc.CardBody(
                                            [
                                                html.H4(
                                                     mark,
                                                    className="card-title",
                                                    style = {  
                                                         'color': 'white',
                                                        "text-transform": "capitalize",
                                                        'justify': 'center',
                                                        'align': 'center',
                                                        'fontWeight': 'bold',
                                                        "fontFamily": "Roboto",
                                                        "display": "block",
                                                        'fontSize':"28px"

                                                    }
                                                ),
                                                
                                                html.Small(
                                                    "Final price: "+ finalp,
                                                        style = {  
                                                         'color': 'white',
                                                        'justify': 'start',
                                                        'align': 'start',
                                                        'fontWeight': 'bold',   
                                                        "fontFamily": "Roboto",
                                                        "display": "block",
                                                        'fontSize':"20px"

                                                    }
                                                ),

                                                html.Small(
                                                    "Origin price: "+ originp,
                                                        style = {  
                                                         'color': 'white',
                                                        'justify': 'start',
                                                        'align': 'start',
                                                        'fontWeight': 'bold',   
                                                        "fontFamily": "Roboto",
                                                        "display": "block",
                                                        'fontSize':"20px"

                                                    }
                                                          ),                                              

                                                html.Small(
                                                    "promotion: "+ promo,
                                                        style = {  
                                                         'color': 'white',
                                                        'justify': 'start',
                                                        'align': 'start',
                                                        'fontWeight': 'bold',   
                                                        "fontFamily": "Roboto",
                                                        "display": "block",
                                                        'fontSize':"20px"

                                                    }
                                                          ),  

                                                  html.P(
                                                description,
                                                className="card-text",
                                                    style = {  
                                                        'color': 'white',
                                                        'justify': 'start',
                                                        'align': 'start',
                                                        'fontWeight': 'bold',
                                                        "fontFamily": "Roboto",
                                                        "display": "block",
                                                        'fontSize':"22px"
                                                    }

                                                ),





                                            ]
                                        ),
                                        className="col-md-8",
                                    ),
                                ],
                                className="g-0 d-flex align-items-center",
                            )
                        
                        
                        ],
                        style={
                            'align': 'center',
                            "width": "800px",
                            "height": "600px",
                            'padding': '15px',
                            "margin": "20px"
                            },
                    )
                 ]
                  ),
        
                    ])