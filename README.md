# Stock-exchange

Program that analyzes the value of shares on the stock exchange, assesses the risk of buying a stock, and determines its ability to grow<br/>

The numpy and scipy.stats libraries to calculate the risk metrics.<br/>
Implemented the analyze_stock() function to calculate the following risk metrics:<br/>

Volatility: Calculates the 20-day rolling standard deviation of daily returns and annualizes it to get the stock's volatility.<br/>
Sharpe Ratio: Calculates the Sharpe ratio, which is the ratio of the mean daily return to the volatility. This provides a measure of the stock's risk-adjusted return.<br/>
Value at Risk (95%): Calculates the 95% Value at Risk, which represents the maximum expected loss over a given time horizon at a given confidence level.<br/>
Risk Assessment: Categorizes the risk level as "Low", "Medium", or "High" based on the stock's volatility.<br/>
Growth Potential: Assesses the growth potential by comparing the 20-day and 50-day moving averages. If the 20-day moving average is higher than the 50-day moving average, the growth potential is considered "Yes".<br/>

