import yfinance as yf
import pandas as pd

def get_price_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df = df[['Close']].dropna()
    df.columns = ['Price']
    return df

if __name__ == "__main__":
    df = get_price_data("NG=F", "2020-01-01", "2024-12-31")
    print(df.head())
    df.to_csv("price_data.csv")