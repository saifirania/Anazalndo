from dash import dcc,html
import dash_bootstrap_components as dbc
from dash import Input, Output,  html,State
from maindash import app
from dash import dcc
import plotly.express as px

from views.product import make_product_card


from mycontrollers.preprocessing import get_df_products
from mycontrollers.preprocessing import select_products

from mycontrollers.priceController import select_moyens_products







def make_list_prods (df_products):
      list_cards = []
      for k, v in df_products.iterrows():
         list_cards.append( make_product_card(v["product"],v["description"],v["sexe"],v["mark"],v["picture"],str(v["finalprice"]),str(v["originprice"]),str(v["promo"])+ "%") )
      return list_cards

df = get_df_products()
def price_average():
      return   html.Div(
                        [
                              html.Br(),
                              html.H6("Select your sexe"),
                              dcc.Dropdown(
                                          ["homme","femme"],
                                          "homme",
                                          id='select_sexe_price_average',
                              ),
                              html.Br(),
                              html.H6("Select your product"),

                              dcc.Dropdown(
                                          sorted(set(df['product'].tolist())),
                                          "chemise",
                                          id='select_product_price_average',
                                          ),
                              html.Br(),
                              html.Br(),


                              
                              html.Div(id="output_choice_price_average"),

                        ]
                         )
    



@app.callback(
              Output('output_choice_price_average', 'children'),
              Input('select_sexe_price_average', 'value'),
              Input('select_product_price_average', 'value'),
              )
def filter_average(sexe,prod):

    if  sexe == [] or  prod == [] :   
        return  html.H1("You lust choose your sexe and your product !")
    else :
        
        df = get_df_products()
        selected_df = select_products(df,prod,sexe, "all")
        df_products = select_moyens_products(selected_df)
        
        return html.Div(
            [
          html.H3("This the list of the products with average price ! " ),
          html.Br(),
          html.Div( make_list_prods(df_products) )

            ]
        )   
         