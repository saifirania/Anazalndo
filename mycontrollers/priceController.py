import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import re
import json



# Price controller for all functions to give all figures for the price view


def give_infos(selected_df):
    # Vision générale basée sur la comparaison liniaire entre (finalprice,originprice,promo)
    return selected_df.quantile([0,.25, .5, .75 ,.99],interpolation='lower')



def select_moins_cher(selected_df):
    # les 5 moins cher 
    moins_cher  = selected_df.sort_values(by=['finalprice'], ascending = True).head(5)
    return moins_cher





def select_plus_cher(selected_df):
    # les 5 plus cher 
    plus_cher  = selected_df.sort_values(by=['finalprice'], ascending = False).head(5)
    return plus_cher



def select_moyens_products(selected_df):
    # Les 5 produits qui representent le milieu de l'ensemble des produits

    # Let’s take a look at the different parameters that the Pandas quantile method offers. The default arguments are provided in square [] brackets.
    # q=[0.5]: a float or an array that provides the value(s) of quantiles to calculate
    # axis=[0]: the axis to calculate the percentiles on (0 for row-wise and 1 for column-wise)
    # numeric_only=[True]: is set to False, calculate the values for datetime and timedelta columns as well
    # interpolation=['linear']: if quantiles exist between two values, how to interpolate the values

    mean_exact = selected_df[selected_df.finalprice == selected_df.quantile(
        q=0.5,                      # The percentile to calculate
        axis=0,                     # The axis to calculate the percentile on
        numeric_only=True,          # To calculate only for numeric columns
        interpolation='lower'      # The type of interpolation to use when the quantile is between 2 values
    ).finalprice].head(3)
    
    return mean_exact






def propose_best_products(selected_df):
    # Proposition de 5 produits qui ont un final price moin ou égale de la moyenne 
    # avec meilleur origin price ou avec meilleur promo 
    q_mean = selected_df.quantile(
        q = 0.5,                      # The percentile to calculate
        axis=0,                     # The axis to calculate the percentile on
        numeric_only=True,          # To calculate only for numeric columns
        interpolation='linear'      # The type of interpolation to use when the quantile is between 2 values
                                )
    
    mean_moins = selected_df[selected_df.finalprice <= q_mean.finalprice]
    mean_moins = mean_moins.sort_values(by=['originprice','promo'], ascending = False).head(10)
    best_products = pd.concat([select_moyens_products(selected_df),mean_moins])
    best_products = best_products.sort_values(by=['originprice','promo'], ascending = False).head(5)
    return best_products