import pandas as pd
import simfin as sf
import service

#TODO: add mypy annotations for the useful_stats, wasn't able to add List[str].

def get_ticker_income(ticker: str, useful_stats = None) -> pd.DataFrame:
  """Sorts income statement so it only has that tickers data.
  Data is indexed by the report date.
  """
  df = service.get_income()
  if useful_stats == None:
      useful_stats = df.columns
  income_df = df.loc[ticker, useful_stats]
  return income_df

def get_ticker_balance(ticker: str, useful_stats = None) -> pd.DataFrame:
  """Sorts balance sheet so it only has that tickers data.
  Data is indexed by the report date.
  """
  df = service.get_balance()
  if useful_stats == None:
      useful_stats = df.columns
  balance_df = df.loc[ticker, useful_stats]
  return balance_df

def get_ticker_cashflow(ticker: str, useful_stats = None) -> pd.DataFrame:
  """Sorts cashflow so it only has that tickers data.
  Data is indexed by the report date.
  """
  df = service.get_cashflow()
  if useful_stats == None:
      useful_stats = df.columns
  cashflow_df = df.loc[ticker, useful_stats]
  return cashflow_df
