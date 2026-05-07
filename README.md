# Energy Risk Model

A Python-based commodity risk model for natural gas (Henry Hub) prices.

## What it does
- Pulls real price data from Yahoo Finance
- Calculates daily and annualized volatility
- Computes 1-Day Value at Risk (VaR) at 95% confidence
- Runs 1,000 Monte Carlo price simulations

## Results
- Annual Volatility: 76.07%
- 1-Day VaR (95%): -6.97% | $-69,681 on $1M position

## Files
- data.py — pulls and stores price data
- returns.py — calculates returns and volatility
- var.py — computes Value at Risk
- monte_carlo.py — runs price simulations
- main.py — runs the full model

## Libraries
pandas, numpy, matplotlib, yfinance, scipy

## How to run
python3 main.py