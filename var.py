import pandas as pd
import numpy as np

def calculate_var(df, confidence=0.95, position_size=1_000_000):
    returns = df['Daily_Return'].dropna()
    var_pct = np.percentile(returns, (1 - confidence) * 100)
    var_dollar = position_size * var_pct
    return var_pct, var_dollar

if __name__ == "__main__":
    df = pd.read_csv("price_data.csv", index_col=0, parse_dates=True)
    df['Daily_Return'] = df['Price'].pct_change().dropna()
    pct, dollar = calculate_var(df)
    print(f"1-Day VaR (95%): {pct:.4f} | ${dollar:,.0f} on $1M position")
    