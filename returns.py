import pandas as pd
import numpy as np

def calculate_returns(df):
    df['Daily_Return'] = df['Price'].pct_change()
    df = df.dropna()
    return df

def calculate_volatility(df):
    daily_vol = df['Daily_Return'].std()
    annual_vol = daily_vol * np.sqrt(252)
    return daily_vol, annual_vol

if __name__ == "__main__":
    df = pd.read_csv("price_data.csv", index_col=0, parse_dates=True)
    df = calculate_returns(df)
    daily, annual = calculate_volatility(df)
    print(f"Daily Volatility:  {daily:.4f}")
    print(f"Annual Volatility: {annual:.4f}")