import pandas as pd
import simfin as sf

# sf.set_api_key('free')
# sf.set_data_dir('./simfin_data/')
# sf.load_balance(variant='quarterly', market='us')
# df = pd.read_csv('./simfin_data/us-shareprices-daily.csv', sep=';')
# tickers = ['GOOG']
# filter = df['Ticker'].isin(tickers)
# print(df.loc[filter])
df = pd.read_csv('./simfin_data/us-balance-quarterly.csv', sep=';')
tickers = ['APPL']
filter = df['Ticker'].isin(tickers)
print(df.loc[filter, ['Fiscal Year', 'Fiscal Period']])
