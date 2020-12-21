import os, sys

import pandas as pd
import numpy as np

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(ROOT_DIR)

from api import service



def get_monthly_averages(df):
  output = {}
  for year in range(df.index[0].year, df.index[-1].year + 1):
    # March
    avg_march = df.loc[f'{year}-03-01' : f'{year}-03-31'].mean()
    if not np.isnan(avg_march):
      output[f'{year}-03'] = avg_march

    # June
    avg_june = df.loc[f'{year}-06-01' : f'{year}-06-30'].mean()
    if not np.isnan(avg_june):
      output[f'{year}-06'] = avg_june

    # September
    avg_september = df.loc[f'{year}-09-01' : f'{year}-09-30'].mean()
    if not np.isnan(avg_september):
      output[f'{year}-09'] = avg_september

    # December
    avg_december = df.loc[f'{year}-12-01' : f'{year}-12-31'].mean()
    if not np.isnan(avg_december):
      output[f'{year}-12'] = avg_december

  return pd.DataFrame.from_dict(output, orient='index', columns=["Monthly Average"])

def write_output(df, ticker):
  ticker_prices = df.loc[ticker, "Close"]
  output =  get_monthly_averages(ticker_prices)

  if not os.path.exists(f'data/{ticker}'):
    os.makedirs(f'data/{ticker}')
  
  output.to_csv(f'data/{ticker}/output.csv')

df_prices = service.get_share_prices()
write_output(df_prices, 'ATVI')

# https://github.com/SimFin/simfin-tutorials/blob/master/09_Machine_Learning.ipynb
