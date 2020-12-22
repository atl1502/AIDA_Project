import os, sys

import pandas as pd
import numpy as np

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(ROOT_DIR)

from api import service


def get_indicator_increase(ticker):
    overall_df = service.get_income()
    ticker_df = overall_df.loc[ticker]
    revenue_df = ticker_df[["Fiscal Year", "Fiscal Period", "Revenue", "Net Income"]]
    return revenue_df

def get_percentage_diff(initial_value, current_value):
    return float((current_value-initial_value)/(initial_value))


def format_indicator_inc(df, indicator):
    output = {}
    counter =1
    for i in range(1, len(df.index)):
        print(df.index[counter]) 
        output[df.index[counter]]  =   get_percentage_diff(df.loc[df.index[counter-1]][indicator], df.loc[df.index[counter]][indicator])
        counter = counter +1
    
    return pd.DataFrame.from_dict(output, orient='index', columns=["Quarterly Change"])


def write_output(ticker, indicator):
    df = get_indicator_increase(ticker)
    to_return = format_indicator_inc(df, "Net Income")

    if not os.path.exists(f'src/data/{ticker}'):
        os.makedirs(f'src/data/{ticker}')
  
    to_return.to_csv(f'src/data/{ticker}/input.csv')



write_output("ATVI", "Net Income")
