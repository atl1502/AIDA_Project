import os
from typing import List
from dotenv import load_dotenv

import pandas as pd
import simfin as sf

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def get_token() -> str:
    """Gets Tiingo API token"""
    load_dotenv()
    return os.getenv("TIINGO_API_TOKEN")


def get_tickers() -> List[str]:
    """Gets tickers in DOW 30"""
    tickers = [
        "AAPL", "AXP", "AMGN", "BA", "CAT", "CSCO", "CVX", "GS", "HD",
        "HON", "IBM", "INTC", "JNJ", "KO", "JPM", "MCD", "MMM", "MRK",
        "MSFT", "NKE", "PG", "TRV", "UNH", "CRM",
        "V", "VZ", "WBA", "WMT", "DIS", "DOW"
    ]

    return tickers


def get_fundamentals(ticker: str, token: str,
                     queries: List[str] = None) -> pd.DataFrame:
    """Gets the fundamentals of a stock

    Includes quarterly data

    Args:
        ticker: ticker that represents stock
        token: API token
        queries: query strings to add to the end of the URL (default: {None})

    Returns:
        Fundamentals of stock if the ticker is in DOW 30,
        or empty dataframe is not in DOW 30 (not covered by free API)
    """
    if queries is None:
        queries = []

    queries.append(f"token={token}&format=csv")
    query = '&'.join(queries)

    url = ("https://api.tiingo.com/tiingo/fundamentals/"
           f"{ticker}/statements?{query}")

    try:
        df = pd.read_csv(url)
    except:
        return pd.DataFrame()
    else:
        return df

def setup_simfin():
  sf.set_api_key('free')
  sf.set_data_dir(os.path.join(ROOT_DIR, 'simfin_data'))

def get_balance() -> pd.DataFrame:
  """Gets the bulk balance statements from SimFin API

  Downloads the data if you don't already have it
  """
  setup_simfin()

  df = sf.load_balance(variant='quarterly', market='us')
  return df

def get_income() -> pd.DataFrame:
  """Gets the bulk income statements from SimFin API

  Downloads the data if you don't already have it
  """
  setup_simfin()
  df = sf.load_income(variant='quarterly', market='us')
  return df

def get_cashflow() -> pd.DataFrame:
  """Gets the bulk cashflow statements from SimFin API

  Downloads the data if you don't already have it
    """
  setup_simfin()
  df = sf.load_cashflow(variant='quarterly', market='us')
  return df

def get_share_prices() -> pd.DataFrame:
  """Gets the bulk share prices from SimFin API

  Downloads the data if you don't already have it
  """
  setup_simfin()
  df = sf.load_shareprices(variant='daily', market='us')
  return df

if __name__ == '__main__':
    token = get_token()
    tickers = get_tickers()

    for ticker in tickers:
        df = get_fundamentals(ticker, token)

        # Ticker is not in DOW 30, which is not covered by free API
        if df.empty:
            continue

        ticker_directory = os.path.join("data", ticker)
        ticker_fundamentals_path = os.path.join(
            ticker_directory, "fundamentals.csv")

        if not os.path.exists(ticker_directory):
            os.makedirs(ticker_directory)

        df.to_csv(ticker_fundamentals_path, index=False)
