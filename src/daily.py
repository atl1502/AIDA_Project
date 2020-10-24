import os, sys

import pandas as pd

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(ROOT_DIR)

from api import service

df_prices = service.get_share_prices()
# df_prices.loc['MSFT', "Close"].plot(grid=True, figsize=(20,10), title='MSFT Close') # need to decide on plotting backend
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
  print(df_prices.loc['MSFT', "Close"])

# https://github.com/SimFin/simfin-tutorials/blob/master/09_Machine_Learning.ipynb
