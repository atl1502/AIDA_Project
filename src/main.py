import input_layer
import daily
import pandas as pd
import numpy as np
import os, sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(ROOT_DIR)

from api import service


## finish function that implements output, input and training from start to finish
## def create_layers: 


def create_training_table(ticker):
    if not os.path.exists(f'src/data/{ticker}'):
        print("Please import data for " + ticker)
        return
    df_input = pd.read_csv(f'src/data/{ticker}/input.csv', index_col=0, parse_dates=True)
    df_output = pd.read_csv(f'src/data/{ticker}/output.csv',index_col=0, parse_dates=True)
    
    df_input.index.name = "date"
    df_input = df_input.reset_index()
    df_input["date"] = df_input["date"].apply(lambda x: x.strftime('%Y-%m'))
    df_input.set_index("date", inplace=True)

    df_output.index.name = "date"
    df_output = df_output.reset_index()
    df_output["date"] = df_output["date"].apply(lambda x: x.strftime('%Y-%m'))
    df_output.set_index("date", inplace=True)


    new_df = pd.merge(df_input,df_output,left_index=True, right_index=True)
    return new_df


def write_training_data(ticker):
    output = create_training_table(ticker)
    if not os.path.exists(f'src/data/{ticker}'):
        os.makedirs(f'src/data/{ticker}')
  
    output.to_csv(f'src/data/{ticker}/trainer.csv')

write_training_data("MSFT")
write_training_data("ATVI")






           