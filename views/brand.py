from dash import dcc,html
import dash_bootstrap_components as dbc
from dash import Input, Output,  html,State
from maindash import app
from dash import dcc
import plotly.express as px

from mycontrollers.preprocessing import get_df_products
from mycontrollers.preprocessing import select_products

from mycontrollers.brandController import get_best_Brands_fig
from mycontrollers.brandController import get_comparaison_fig
from mycontrollers.brandController import get_number_products_fig
from mycontrollers.brandController import get_fig_analyse_brands




rang_slider = 0.5
my_sexe = "homme"
my_product = "chemise"

df = get_df_products()
li_prods =  sorted(set(df['product'].tolist()))


def make_marque():

    return   html.Div(
                        [
                         
                           html.H3("Hello, you can discover new  brands with us !"),
                           html.Br(),
                           html.Br(),
                           html.H6("Select your sexe"),
                           dcc.Dropdown(
                                    ["homme","femme"],
                                    my_sexe,
                                    id='select_sexe',
                            ),
                            html.Br(),
                           html.H6("Select your product"),

                           dcc.Dropdown(
                                    li_prods,
                                    my_product,
                                    id='select_product',
                                       ),
                            html.Br(),
                            html.Br(),
                            html.Br(),

                            html.H4("Analyse top brands prices "),
                            dcc.Graph(id  ="output_res_fig4"),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),


                            html.H4("Products distribution of all brands "),
                            dcc.Graph(id  ="output_res_fig3"),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),



                            html.H4("In this part of our website, you can easily choose a rang "),                           
                            html.H4("on the slider to visualise a special part of the results! "),                           
                            html.H4("for example : rang = 0.5 will give you result based on the 50% quartile of the dataset !"),                           
                            html.H4("Enjoy our interactive graphs :) "),
                            html.Br(),
                            html.Br(),

                            dcc.Slider(0, 1, 0.1,
                                        value=0.5,
                                        id='rang_slider'
                                        ),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),

                            html.H4("Best recommanded brands for you ! "),
                            dcc.Graph(id  ="output_res_fig1"),
                            html.Br(),
                            html.Br(),
                            html.Br(),

                            html.H4("Final and origin price of our recommanded brands ! "),
                            dcc.Graph(id  ="output_res_fig2"),
                            html.Br(),

                            html.Br(),
                            html.Br(),
       
                            
                            


                        ]
                        )
    
@app.callback(
              Output('output_res_fig1', 'figure'),
              Output('output_res_fig2', 'figure'),
              Output('output_res_fig3', 'figure'),
              Output('output_res_fig4', 'figure'),
              Input('select_sexe', 'value'),
              Input('select_product', 'value'),
              Input('rang_slider', 'value')
              )
def filter_countries(sexe,prod,rangs):

    if  sexe == [] or  prod == [] :   
        f =  figure
        return  f

    else :
        my_sexe = sexe
        my_product = prod
        rang_slider = rangs

        selected_df = select_products(df,my_product,my_sexe, "all")
        
        fig1  = get_best_Brands_fig(selected_df,rang_slider) 
        fig2 = get_comparaison_fig(selected_df,rang_slider)
        fig3 = get_number_products_fig(selected_df)
        fig4 = get_fig_analyse_brands(df,selected_df,my_product,my_sexe)
        return fig1 , fig2 , fig3,fig4
