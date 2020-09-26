# import requests
# import json
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

  # token = ""
  # with open("AIDA_Project/Secrets/token.txt", "r") as f:
  #   token = f.read()
  # return token

def get_tickers():
  """Gets tickers in DOW 30

  Returns:
    list -- tickers in DOW 30
  """
  tickers = ["AAPL", "AXP", "AMGN", "BA", "CAT", "CSCO", "CVX", "GS", "HD", "HON", "IBM", "INTC",
           "JNJ", "KO","JPM", "MCD", "MMM", "MRK", "MSFT", "NKE", "PG", "TRV", "UNH", "CRM",
           "V", "VZ", "WBA", "WMT", "DIS", "DOW"]
  return tickers


def get_fundamentals(ticker, token, queries=[]):
  """Gets the fundamentals of a stock

  Includes quarterly data

  Arguments:
    ticker {string} -- ticker that represents stock
    token {string} -- API token
    queries {list} -- query strings to add to the end of the URL

  Returns:
    pd.DataFrame -- Fundamentals of stock
  """

  queries.append(f"token={token}&format=csv")
  query = f"{'&'.join(queries)}"

  url = f"https://api.tiingo.com/tiingo/fundamentals/{ticker}/statements?{queries}"

  return pd.read_csv(url)

"""
# Saves all the tickers in DOW30 to json file
headers = {
    'Content-Type': 'application/json'
}

for ticker in tickers:
    endpoint_fundamentals = f"https://api.tiingo.com/tiingo/fundamentals/{ticker}/statements"

    request_response = requests.get(f"{endpoint_fundamentals}?token={token}",
                                    headers=headers).json()
    with open(f"AIDA_Project/Secrets/{ticker}_financials.json", "w") as f:
        f.write(json.dumps(request_response, indent=2))
"""

if __name__ == '__main__':
  token = get_token()
  tickers = get_tickers()

  for ticker in tickers:
    df = get_fundamentals(ticker, token)
    df.to_csv(os.path.join("data", ticker, "fundamentals")) # or os.path.join("data", "fundamentals", ticker)