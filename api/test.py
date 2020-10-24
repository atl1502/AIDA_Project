import pandas as pd
import simfin as sf
from pandas import DataFrame
import matplotlib.pyplot as plt

sf.set_api_key('free')
sf.set_data_dir('./api/data/')
sf.load_balance(variant='quarterly', market='us')



df = pd.read_csv('./api/data/us-balance-quarterly.csv', sep=';')
tickers = ['AAPL']
filter = df['Ticker'].isin(tickers)

newdf = df.loc[filter, ['Fiscal Year', 'Fiscal Period', 'Retained Earnings']]

newdf.plot(x='Fiscal Year', y='Retained Earnings', kind='bar')


plt.title("AAPL Earnings/Fiscal Quarter") 
plt.show()





print(newdf)





