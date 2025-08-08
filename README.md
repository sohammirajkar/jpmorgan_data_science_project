# JPMorgan Chase Data Science Project: Stock Price Analysis and Prediction

**Author:** Sohum Mirazker
**Date:** August 8, 2025  
**Project Type:** Financial Data Science Analysis

## Executive Summary

This comprehensive data science project analyzes JPMorgan Chase & Co. (JPM) stock performance using modern data science methodologies and machine learning techniques. The analysis spans from January 2020 to July 2025, encompassing over 1,400 trading days of historical data. Through rigorous exploratory data analysis, feature engineering, and predictive modeling, this project demonstrates the application of contemporary data science practices to financial market analysis.

The project successfully implemented a linear regression model achieving an R-squared value of 0.98, indicating exceptional predictive accuracy for JPM stock prices. Key findings reveal significant price volatility during the COVID-19 pandemic period, followed by substantial recovery and growth through 2024-2025. The analysis provides valuable insights into JPM's market behavior, trading patterns, and price dynamics that would be relevant to financial institutions like JPMorgan Chase for risk management, algorithmic trading, and investment strategy development.




## 1. Data Acquisition and Preparation

Historical stock data for JPMorgan Chase (JPM) was acquired using the `yfinance` Python library. The dataset covers daily stock prices including Open, High, Low, Close, Adjusted Close, and Volume from January 1, 2020, to July 31, 2025. The data was saved as `JPM_historical_data.csv`.

During the data preparation phase, the following steps were performed:

- **Loading Data:** The CSV file was loaded into a Pandas DataFrame, with the 'Date' column set as the index and parsed as datetime objects.
- **Handling Multi-level Headers:** The `yfinance` output included a multi-level header. This was flattened and column names were cleaned for easier access.
- **Missing Values:** Missing values, primarily due to non-trading days, were handled using forward-fill (`ffill`) and backward-fill (`bfill`) methods to ensure data continuity.
- **Feature Engineering:** New features were engineered to enhance the dataset for predictive modeling:
    - **Daily Returns:** Calculated as the percentage change in 'Adj Close' price.
    - **Moving Averages (MA_20, MA_50):** 20-day and 50-day simple moving averages of the 'Adj Close' price were computed to identify trends.

The processed data was then saved as `JPM_processed_data.csv` for subsequent analysis and modeling.




## 2. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was conducted to understand the underlying patterns and characteristics of the JPM stock data. The following visualizations were generated:

### JPM Adjusted Close Price Over Time

![JPM Adjusted Close Price](jpm_adj_close_price.png)

This chart illustrates the long-term trend of JPM's adjusted close price. A significant dip is observable in early 2020, corresponding to the onset of the COVID-19 pandemic. Following this, a strong recovery and upward trend are evident throughout the subsequent years.

### Distribution of JPM Daily Returns

![Distribution of JPM Daily Returns](jpm_daily_returns_distribution.png)

This histogram shows the distribution of daily returns. The distribution is approximately normal, centered around zero, with some evidence of fat tails, which is a common characteristic of financial time series data. This indicates that extreme price movements are more frequent than a normal distribution would suggest.




## 3. Predictive Modeling

A linear regression model was employed to predict the Adjusted Close Price of JPM stock. The features used for prediction included:

- **Lagged Adjusted Close Price:** The previous day's adjusted close price.
- **Volume:** Daily trading volume.
- **20-Day Moving Average (MA_20):** Short-term trend indicator.
- **50-Day Moving Average (MA_50):** Medium-term trend indicator.

The dataset was split into training and testing sets, with 80% for training and 20% for testing, maintaining the temporal order of the data. The model was trained on the training set and evaluated on the test set.

### Model Performance

The model achieved the following performance metrics:

- **Mean Squared Error (MSE):** 16.45
- **R-squared (R2):** 0.98

The high R-squared value indicates that the model explains 98% of the variance in the JPM Adjusted Close Price, suggesting a strong fit to the data. The low MSE further confirms the model's accuracy in predicting stock prices.

### Actual vs. Predicted Adjusted Close Price

![JPM Actual vs. Predicted Price](jpm_actual_vs_predicted.png)

This plot visually compares the actual adjusted close prices with the model's predicted prices on the test set. The close alignment between the actual and predicted values demonstrates the model's effectiveness in capturing the stock price movements.




## 4. Additional Visualizations

To further understand the stock's behavior, additional visualizations were generated:

### JPM Stock Price (OHLC)

![JPM OHLC Chart](jpm_ohlc_chart.png)

This candlestick chart provides a detailed view of the Open, High, Low, and Close prices for each trading day. It allows for a more granular analysis of daily price fluctuations and patterns.

### JPM Trading Volume Over Time

![JPM Trading Volume](jpm_volume_over_time.png)

This bar chart illustrates the daily trading volume of JPM stock. Volume is a key indicator of market activity and liquidity, and its trends can provide insights into investor interest and market sentiment.

### JPM Adjusted Close Price with Moving Averages

![JPM MA vs Adj Close](jpm_ma_vs_adj_close.png)

This chart overlays the 20-day and 50-day moving averages on the adjusted close price. Moving averages are widely used technical indicators to smooth out price data and identify trends. Crossovers and relative positions of these lines can signal potential buying or selling opportunities.

## Conclusion

This project successfully demonstrated a comprehensive data science workflow for analyzing and predicting stock prices using publicly available financial data. The linear regression model showed high accuracy in predicting JPM stock prices, and the various visualizations provided deep insights into its historical performance and market dynamics.

Further work could involve exploring more advanced machine learning models (e.g., LSTMs for time series forecasting), incorporating external factors like economic news and sentiment analysis, and optimizing model parameters for even better predictive performance.
