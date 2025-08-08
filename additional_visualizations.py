import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Loads data from a CSV file."""
    df = pd.read_csv(file_path, index_col="Date", parse_dates=True)
    return df

def create_additional_visualizations(df):
    """Creates additional visualizations for the processed data."""
    # Candlestick chart for a closer look at price movements
    plt.figure(figsize=(15, 7))
    plt.plot(df.index, df["Open"], label="Open")
    plt.plot(df.index, df["High: JPM"]) # This line was causing the error
    plt.plot(df.index, df["Low: JPM"]) # This line was causing the error
    plt.plot(df.index, df["Close: JPM"]) # This line was causing the error
    plt.title("JPM Stock Price (OHLC)")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.savefig("jpmorgan_data_science_project/jpm_ohlc_chart.png")
    plt.close()

    # Volume over time
    plt.figure(figsize=(15, 7))
    plt.bar(df.index, df["Volume"], color="skyblue")
    plt.title("JPM Trading Volume Over Time")
    plt.xlabel("Date")
    plt.ylabel("Volume")
    plt.grid(True)
    plt.savefig("jpmorgan_data_science_project/jpm_volume_over_time.png")
    plt.close()

    # Moving Averages vs. Adjusted Close Price
    plt.figure(figsize=(15, 7))
    plt.plot(df.index, df["Adj Close"], label="Adj Close")
    plt.plot(df.index, df["MA_20"], label="20-Day MA")
    plt.plot(df.index, df["MA_50"], label="50-Day MA")
    plt.title("JPM Adjusted Close Price with Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Adjusted Close Price")
    plt.legend()
    plt.grid(True)
    plt.savefig("jpmorgan_data_science_project/jpm_ma_vs_adj_close.png")
    plt.close()

    print("Additional visualizations created: jpm_ohlc_chart.png, jpm_volume_over_time.png, jpm_ma_vs_adj_close.png")