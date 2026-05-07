from data import get_price_data
from returns import calculate_returns, calculate_volatility
from var import calculate_var
from monte_carlo import monte_carlo_simulation
import matplotlib.pyplot as plt

df = get_price_data("NG=F", "2020-01-01", "2024-12-31")
df.to_csv("price_data.csv")

df = calculate_returns(df)
daily_vol, annual_vol = calculate_volatility(df)
var_pct, var_dollar = calculate_var(df)

print("=== COMMODITY RISK SUMMARY ===")
print(f"Annual Volatility:  {annual_vol:.2%}")
print(f"1-Day VaR (95%):    {var_pct:.2%} | ${var_dollar:,.0f} on $1M")

last_price = df['Price'].iloc[-1]
sims = monte_carlo_simulation(last_price, daily_vol)

plt.figure(figsize=(12,6))
plt.plot(sims[:100].T, alpha=0.3, color='steelblue')
plt.title("Natural Gas Monte Carlo Simulation")
plt.savefig("monte_carlo.png")
plt.show()