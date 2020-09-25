import requests
import json
"""
Setup:
have a folder called Secrets, it'll hold your personal token and the data pulled from the API. In it you need a file token.txt that will hold the token in it. Secrets is added to the gitignore so it won't show up when typing git status.
"""
# Pulls token from file
with open("AIDA_Project/Secrets/token.txt", "r") as f:
    token = f.read()

# List of tickers in the DOW30
tickers = ["AAPL", "AXP", "AMGN", "BA", "CAT", "CSCO", "CVX", "GS", "HD", "HON", "IBM", "INTC", "JNJ", "KO",
           "JPM", "MCD", "MMM", "MRK", "MSFT", "NKE", "PG", "TRV", "UNH", "CRM", "V", "VZ", "WBA", "WMT", "DIS", "DOW"]


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
