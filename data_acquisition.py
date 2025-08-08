import yfinance as yf
import pandas as pd

def get_jpm_data(ticker="JPM", start_date="2020-01-01", end_date="2025-07-31"):
    """Fetches historical stock data for JPM."""
    data = yf.download(ticker, start=start_date, end=end_date)
    if data is not None and not data.empty:
        data.to_csv(f"{ticker}_historical_data.csv")
        print(f"Downloaded {ticker} data from {start_date} to {end_date} and saved to {ticker}_historical_data.csv")
        return data
    else:
        print(f"Failed to download data for {ticker}")
        return None

if __name__ == "__main__":
    get_jpm_data()