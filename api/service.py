import os
from typing import List
from dotenv import load_dotenv
import pandas as pd


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
