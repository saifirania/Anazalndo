import pandas as pd
import os
import json
import re
import plotly.express as px
import plotly.graph_objs as go
import plotly.graph_objects as go
from mycontrollers.preprocessing import select_products







# BRAND controller for all functions to give all figures for the brand view


def get_Brands(selected_df,selected_rang):
    marks_cout = selected_df.groupby(["mark"]).mean()
    q_mean = marks_cout.quantile(
        q = selected_rang,                      # The percentile to calculate
        axis=0,                     # The axis to calculate the percentile on
        numeric_only=True,          # To calculate only for numeric columns
        interpolation='linear'      # The type of interpolation to use when the quantile is between 2 values
                                )

    df_res = marks_cout[marks_cout.finalprice <= q_mean.finalprice]
    df_res = df_res.sort_values(by=['finalprice',"originprice","promo"], ascending = False).head(5)
    df_res.reset_index(inplace=True)
    return df_res


def get_best_Brands_fig(selected_df,selected_rang):
    df_res = get_Brands(selected_df, selected_rang)
    fig = px.histogram(
                        df_res,
                         x="mark",
                         y="promo",
                         color ="mark",
                         template='plotly_dark',
                         title="Best brands based on linear function(final price , origin price, promo ) ",
                         labels={'mark':'Brand',"y": "origin price"}, 
                         height=600
                      )
    return fig




# ******************************************************************************************************************************

def get_comparaison_fig(selected_df,selected_rang):
    df_res = get_Brands(selected_df, selected_rang)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x= df_res["mark"],
        y=df_res["originprice"],
        name='origin price',
        marker_color='green',
    ))
    fig.add_trace(go.Bar(
        x= df_res["mark"],
        y=df_res["finalprice"],
        name='final price',
        marker_color='red',

    ))

    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    fig.update_layout(
        barmode='group', 
         template='plotly_dark',
         title="Best brands prices comparaison based on linear function(final price , origin price, promo ) ",
         height=600    
    )
    return fig


# ******************************************************************************************************************************

def get_number_products_df (selected_df):
    marks_count = selected_df.groupby(["mark"]).count()
    marks_count.reset_index(inplace=True)
    marks_count["number_products"] =  marks_count["product"]
    marks_count = marks_count.sort_values(by='number_products', ascending = False)
    marks_count.reset_index(inplace=True)
    marks_count = marks_count[["mark","number_products"]]
    return marks_count
def get_number_products_fig (selected_df):
    marks_count = get_number_products_df (selected_df)
    fig = px.pie(
                    marks_count.head(10), 
                    values='number_products',
                    names='mark', 
                    title='Number products on Brand ',
                    template='plotly_dark'
                            )
    return fig

# ******************************************************************************************************************************

def get_df_trendbrand(trend_brands,df,product,sexe):
    df_res = pd.DataFrame()
    for brand in trend_brands :
            selected_df = select_products(df,product,sexe,brand )
            df_res = pd.concat([df_res,selected_df])
    return df_res


# function 3
def get_fig_analyse_brands(df_origin , selected_df,my_product,my_sexe):
    trend_brands = get_number_products_df(selected_df).head(5)["mark"].tolist()
    final_sel_df = get_df_trendbrand(trend_brands,df_origin,my_product,my_sexe)
    fig1 = px.scatter(final_sel_df, 
                     x="mark",
                     y="finalprice",
                     size="promo", 
                     color="mark",
                     log_x=False, 
                     size_max=40,
                     template='plotly_dark',
                     title="Analysing all brands distibution prices",
                     labels={"finalprice": "Price",'mark':'Brand'}, 
                     height=600,

                    )
    return fig1
# ******************************************************************************************************************************