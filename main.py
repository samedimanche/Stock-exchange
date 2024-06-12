import matplotlib
matplotlib.use('TkAgg')  # Set the backend to 'TkAgg' or 'Qt5Agg'
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import numpy as np
from scipy.stats import norm

def get_stock_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data

def analyze_stock(data, ticker):
    # Calculate daily returns
    data['Daily Return'] = data['Close'].pct_change()

    # Calculate cumulative returns
    data['Cumulative Return'] = (1 + data['Daily Return']).cumprod()

    # Calculate moving averages
    data['MA20'] = data['Close'].rolling(window=20).mean()
    data['MA50'] = data['Close'].rolling(window=50).mean()

    # Display summary statistics
    print("Summary Statistics:")
    print(data.describe())

    # Calculate risk metrics
    data['Volatility'] = data['Daily Return'].rolling(window=20).std() * np.sqrt(252)
    data['Sharpe Ratio'] = data['Daily Return'].mean() / data['Volatility']
    data['Value at Risk (95%)'] = -data['Daily Return'].rolling(window=252).quantile(0.05)

    # Assess risk and growth potential
    risk_level = "Low" if data['Volatility'].iloc[-1] < 0.15 else "Medium" if data['Volatility'].iloc[-1] < 0.25 else "High"
    growth_potential = "Yes" if data['MA20'].iloc[-1] > data['MA50'].iloc[-1] else "No"

    print(f"Risk Level: {risk_level}")
    print(f"Growth Potential: {growth_potential}")

    # Plot stock price and moving averages
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Closing Price')
    plt.plot(data['MA20'], label='20-Day Moving Average')
    plt.plot(data['MA50'], label='50-Day Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f"{ticker} Stock Price")
    plt.legend()
    plt.show()

    # Plot cumulative returns
    plt.figure(figsize=(12, 6))
    plt.plot(data['Cumulative Return'], label='Cumulative Return')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.title(f"{ticker} Cumulative Return")
    plt.legend()
    plt.show()

    # Plot risk metrics
    # plt.figure(figsize=(12, 6))
    # plt.plot(data['Volatility'], label='Volatility')
    # plt.plot(data['Sharpe Ratio'], label='Sharpe Ratio')
    # plt.plot(data['Value at Risk (95%)'], label='Value at Risk (95%)')
    # plt.xlabel('Date')
    # plt.ylabel('Metric')
    # plt.title(f"{ticker} Risk Metrics")
    # plt.legend()
    # plt.show()

# Prompt the user for stock information
ticker = input("Enter the stock ticker symbol: ")
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Get stock data
stock_data = get_stock_data(ticker, start_date, end_date)

# Analyze the stock data
analyze_stock(stock_data, ticker)
