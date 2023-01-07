from dash import dcc,html
import dash_bootstrap_components as dbc
from dash import Input, Output,  html,State
from maindash import app
from dash import dcc
import plotly.express as px

from views.product import make_product_card


from mycontrollers.preprocessing import get_df_products
from mycontrollers.preprocessing import select_products

from mycontrollers.priceController import select_moins_cher







def make_list_prods (df_products):
      list_cards = []
      for k, v in df_products.iterrows():
         list_cards.append( make_product_card(v["product"],v["description"],v["sexe"],v["mark"],v["picture"],str(v["finalprice"]),str(v["originprice"]),str(v["promo"])+ "%") )
      return list_cards

df = get_df_products()
def price_cheap():
      return   html.Div(
                        [
                              html.Br(),
                              html.H6("Select your sexe"),
                              dcc.Dropdown(
                                          ["homme","femme"],
                                          "homme",
                                          id='select_sexe_price_cheap',
                              ),
                              html.Br(),
                              html.H6("Select your product"),

                              dcc.Dropdown(
                                          sorted(set(df['product'].tolist())),
                                          "chemise",
                                          id='select_product_price_cheap',
                                          ),
                              html.Br(),
                              html.Br(),


                              
                              html.Div(id = 'output_choice_price_cheap' )
                        ]



                        
                         )
    

@app.callback(
              Output('output_choice_price_cheap', 'children'),
              Input('select_sexe_price_cheap', 'value'),
              Input('select_product_price_cheap', 'value'),
              )
def filter_cheap(sexe,prod):
    if  sexe == [] or  prod == []:   
        return  html.H1("You lust choose your sexe and your product !")
    else :
        df = get_df_products()
        selected_df = select_products(df,prod,sexe, "all")      
        df_products = select_moins_cher(selected_df)
        return html.Div(
                  [
                              html.H3("This the list of the products with cheap price ! " ),
                              html.Br(),
                              html.Div(make_list_prods(df_products) ) 
                  ]
        )
        