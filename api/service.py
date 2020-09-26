import os
import pandas as pd
from dotenv import load_dotenv

def get_token():
  """Gets Tiingo API token

  Returns:
    string -- API token
  """
  load_dotenv();
  return os.getenv("TIINGO_API_TOKEN")

def get_tickers(): # TODO: Update DOW 30 tickers to match actual DOW 30 (some are not so free API doesnt work)
  """Gets tickers in DOW 30

  Returns:
    list -- tickers in DOW 30
  """
  tickers = ["AAPL", "AXP", "AMGN", "BA", "CAT", "CSCO", "CVX", "GS", "HD", "HON", "IBM", "INTC",
           "JNJ", "KO","JPM", "MCD", "MMM", "MRK", "MSFT", "NKE", "PG", "TRV", "UNH", "CRM",
           "V", "VZ", "WBA", "WMT", "DIS", "DOW"]
  return tickers


def get_fundamentals(ticker, token, queries=None):
  """Gets the fundamentals of a stock

  Includes quarterly data

  Arguments:
    ticker {string} -- ticker that represents stock
    token {string} -- API token
    queries {list} -- query strings to add to the end of the URL

  Returns:
    pd.DataFrame -- Fundamentals of stock if the ticker is in DOW 30,
                    or empty dataframe is not in DOW 30 (not covered by free API)
  """
  if queries is None:
    queries = []

  queries.append(f"token={token}&format=csv")
  query = '&'.join(queries)

  url = f"https://api.tiingo.com/tiingo/fundamentals/{ticker}/statements?{query}"

  try:
    return pd.read_csv(url)
  except:
    return pd.DataFrame()

if __name__ == '__main__':
  token = get_token()
  tickers = get_tickers()

  for ticker in tickers:
    df = get_fundamentals(ticker, token)

    # ticker is not in DOW 30, which is not covered by free API
    if df.empty:
      continue

    ticker_directory = os.path.join("data", ticker)
    ticker_fundamentals_path = os.path.join(ticker_directory, "fundamentals.csv")

    if not os.path.exists(ticker_directory):
      os.makedirs(ticker_directory)

    df.to_csv(ticker_fundamentals_path, index=False)