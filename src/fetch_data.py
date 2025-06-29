# Get earnings + yfinance data for a given stock ticker

import yfinance as yf
import pandas as pd
import os


def fetch_stock_data(
    ticker="COIN", period="2y", interval="1d", save_path="data/stock_data.csv"
):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    stock = yf.Ticker(ticker)

    # Fetch historical market data
    hist = stock.history(period=period, interval=interval)

    # Save to CSV
    hist.to_csv(save_path)
    print(f"Saved stock data to {save_path}")


if __name__ == "__main__":
    fetch_stock_data()
