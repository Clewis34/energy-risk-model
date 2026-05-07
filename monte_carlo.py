import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def monte_carlo_simulation(last_price, daily_vol, days=252, simulations=1000):
    results = []
    for _ in range(simulations):
        prices = [last_price]
        for _ in range(days):
            shock = np.random.normal(0, daily_vol)
            prices.append(prices[-1] * (1 + shock))
        results.append(prices)
    return np.array(results)

if __name__ == "__main__":
    df = pd.read_csv("price_data.csv", index_col=0, parse_dates=True)
    last_price = df['Price'].iloc[-1]
    daily_vol = df['Price'].pct_change().dropna().std()

    simulations = monte_carlo_simulation(last_price, daily_vol)

    plt.figure(figsize=(12, 6))
    plt.plot(simulations[:100].T, alpha=0.3, color='steelblue')
    plt.title("Natural Gas Price Monte Carlo Simulation (1000 paths)")
    plt.xlabel("Trading Days")
    plt.ylabel("Price ($/MMBtu)")
    plt.tight_layout()
    plt.savefig("monte_carlo.png")
    plt.show()