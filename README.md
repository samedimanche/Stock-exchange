# Stock Exchange Analysis Tool

This project is a **Python-based program** designed to analyze the value of stocks on the stock exchange, assess the risk of purchasing a stock, and determine its potential for growth. It leverages financial data from **Yahoo Finance** and uses statistical libraries to calculate key risk metrics. This tool was developed **for educational purposes only** and is not intended for commercial use. The author is not responsible for any financial losses, as this project is designed to explore the capabilities of Python libraries and is not a financial recommendation.

---

## Overview

The program provides a comprehensive analysis of a stock's performance by calculating and visualizing key metrics such as volatility, Sharpe ratio, and Value at Risk (VaR). It also assesses the stock's growth potential by comparing short-term and long-term moving averages. The results are presented in an easy-to-understand format, complete with visualizations.

---

## Features

- **Stock Data Retrieval**: Fetches historical stock data using the `yfinance` library.
- **Risk Metrics Calculation**:
  - **Volatility**: Measures the stock's price fluctuations over time.
  - **Sharpe Ratio**: Evaluates the risk-adjusted return of the stock.
  - **Value at Risk (95%)**: Estimates the maximum potential loss at a 95% confidence level.
- **Risk Assessment**: Categorizes the stock's risk level as **Low**, **Medium**, or **High** based on its volatility.
- **Growth Potential**: Determines growth potential by comparing the 20-day and 50-day moving averages.
- **Visualizations**:
  - Plots the stock's closing price along with its 20-day and 50-day moving averages.
  - Displays the cumulative return over the specified time period.

---

## Technologies Used

- **Python**: The core programming language used for the project.
- **yfinance**: A library to fetch historical stock data from Yahoo Finance.
- **NumPy**: Used for numerical calculations, including volatility and Sharpe ratio.
- **SciPy**: Provides statistical functions for calculating Value at Risk (VaR).
- **Pandas**: Used for data manipulation and analysis.
- **Matplotlib**: Used for visualizing stock data and analysis results.

---

## How It Works

1. **User Input**: The program prompts the user to input the stock ticker symbol, start date, and end date.
2. **Data Retrieval**: The program fetches historical stock data using the `yfinance` library.
3. **Data Analysis**:
   - Calculates daily returns, cumulative returns, and moving averages.
   - Computes risk metrics such as volatility, Sharpe ratio, and Value at Risk (95%).
   - Assesses the stock's risk level and growth potential.
4. **Visualization**:
   - Plots the stock's closing price along with its 20-day and 50-day moving averages.
   - Displays the cumulative return over the specified time period.
5. **Output**: Prints summary statistics, risk level, and growth potential.

---

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Stock-exchange.git
   cd Stock-exchange
   ```

2. **Install Dependencies**:
   - Install the required libraries using `pip`:
     ```bash
     pip install yfinance numpy scipy pandas matplotlib
     ```

3. **Run the Program**:
   ```bash
   python main.py
   ```

4. **Input Stock Information**:
   - Enter the stock ticker symbol (e.g., `AAPL`).
   - Enter the start date (e.g., `2022-01-01`).
   - Enter the end date (e.g., `2023-01-01`).

---

## Example Output

### Summary Statistics
```
Summary Statistics:
              Open        High         Low       Close    Volume  Daily Return  Cumulative Return  MA20  MA50  Volatility  Sharpe Ratio  Value at Risk (95%)
count  252.000000  252.000000  252.000000  252.000000  252.000000    251.000000         251.000000  233.0  203.0  233.000000    233.000000           233.000000
mean   150.000000  152.000000  148.000000  150.000000  1000000.000      0.001000           1.200000  150.0  150.0    0.200000      0.500000            -0.020000
std     10.000000   10.000000   10.000000   10.000000   500000.000      0.010000           0.100000   10.0   10.0    0.050000      0.100000             0.010000
min    130.000000  132.000000  128.000000  130.000000   500000.000     -0.050000           1.000000  130.0  130.0    0.100000      0.300000            -0.040000
max    170.000000  172.000000  168.000000  170.000000  2000000.000      0.050000           1.500000  170.0  170.0    0.300000      0.700000            -0.010000
```

### Risk and Growth Assessment
```
Risk Level: Medium
Growth Potential: Yes
```

### Visualizations
- **Stock Price and Moving Averages**: Displays the stock's closing price along with its 20-day and 50-day moving averages.
- **Cumulative Return**: Shows the cumulative return over the specified time period.

---

## Disclaimer

This project was developed **for educational purposes only**. It is not intended for commercial use, and no part of this project is monetized. The author is not responsible for any financial losses incurred as a result of using this tool. This project is designed to explore the capabilities of Python libraries and is not a financial recommendation.

---

## Contribution

Contributions to the project are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Thank you for your interest in this project! For more details, feel free to explore the repository and reach out with any questions.
