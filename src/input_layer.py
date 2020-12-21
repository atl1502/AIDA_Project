import os, sys

import pandas as pd
import numpy as np

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(ROOT_DIR)

from api import service


def get_revenue_increase(ticker):
    overall_df = service.get_income()
    ticker_df = overall_df.loc[ticker]
    revenue_df = ticker_df[["Fiscal Year", "Fiscal Period", "Revenue", "Net Income"]]
    print(revenue_df)
    return revenue_df


ticker = 'AAPL'
df = get_revenue_increase(ticker)



def format_revenue_inc(df):
    output = {}
    