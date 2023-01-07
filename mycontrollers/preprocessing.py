import pandas as pd
import os
import json
import re
pd.options.mode.chained_assignment = None 



# pre processing  
def treat_finalprice(x):
    x = x.replace("," , ".")
    float_regex = "[-+]?[0-9]*\.?[0-9]*"
    match = re.findall(float_regex, x)
    if match[0] != "":
        x = float(match[0])
    return x

def treating_prices(df):
    df['finalprice'] = df['finalprice'].apply(lambda x: treat_finalprice(x))
    df['originprice'] = df['originprice'].apply(lambda x: treat_finalprice(x))
    return df

def preprocess_df(df):
    df = df[['product', 'picture','sexe','mark', 'description','finalprice', 'originprice', 'promo',]]
    df = treating_prices(df)
    return df

def get_df_products():
    path = os.getcwd()+"\\data\\all_data_result_final.csv"
    df = pd.read_csv(path)
    # df = preprocess_df(df)
    return  df




# Start managing our Data
def select_products(df,product,sexe, mark): 
    if product == "all" and sexe == "all" and mark == "all":
        df_res = df
    elif product == "all":
        df_res = df[(df['sexe'] == sexe) & (df['mark'] == mark) ]
    elif sexe == "all":
        df_res = df[(df['product'] == product) & (df['mark'] == mark) ]
    elif mark == "all":
        df_res = df[(df['product'] == product) & (df['sexe'] == sexe) ]
        
    elif product == "all" and sexe == "all":
        df_res = df[(df['mark'] == mark) ]
    elif product == "all" and mark == "all":
        df_res = df[(df['sexe'] == sexe) ]
        
    elif sexe == "all" and mark == "all":
        df_res = df[(df['product'] == product) ]
    else :
        df_res = df[ (df['product'] == product) & (df['sexe'] == sexe) & (df['mark'] == mark) ]
        
    return df_res




