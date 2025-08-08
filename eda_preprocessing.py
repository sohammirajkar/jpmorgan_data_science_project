import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Loads data from a CSV file, handling the multi-level header."""
    df = pd.read_csv(file_path, header=[0, 1], index_col=0, parse_dates=True)
    # Flatten the multi-level columns and clean up names
    df.columns = [f"{col[0]} {col[1]}".strip() if col[1] else col[0].strip() for col in df.columns]
    print("Columns after flattening:", df.columns) # Debugging line
    df.rename(columns={
        'Close JPM': 'Close',
        'High JPM': 'High',
        'Low JPM': 'Low',
        'Open JPM': 'Open',
        'Volume JPM': 'Volume',
        'Adj Close JPM': 'Adj Close' # Corrected for yfinance output
    }, inplace=True)
    # If 'Adj Close' is not present, use 'Close' as 'Adj Close' for now
    if 'Adj Close' not in df.columns:
        df['Adj Close'] = df['Close']
    return df

def perform_eda(df):
    """Performs basic EDA and prints information."""
    print("\n--- Data Info ---")
    df.info()
    print("\n--- Descriptive Statistics ---")
    print(df.describe())
    print("\n--- Missing Values ---")
    print(df.isnull().sum())

def preprocess_data(df):
    """Handles missing values (if any) and creates new features."""
    # For stock data, often missing values are due to non-trading days, forward fill is common
    df_processed = df.copy()
    df_processed.fillna(method='ffill', inplace=True)
    df_processed.fillna(method='bfill', inplace=True) # In case of leading NaNs

    # Feature Engineering: Daily Returns
    df_processed['Daily_Return'] = df_processed['Adj Close'].pct_change()

    # Feature Engineering: Moving Averages
    df_processed['MA_20'] = df_processed['Adj Close'].rolling(window=20).mean()
    df_processed['MA_50'] = df_processed['Adj Close'].rolling(window=50).mean()

    print("\n--- Data after Preprocessing ---")
    print(df_processed.head())
    return df_processed

def visualize_data(df):
    """Creates basic visualizations."""
    plt.figure(figsize=(12, 6))
    plt.plot(df["Adj Close"])
    plt.title("JPM Adjusted Close Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Adjusted Close Price")
    plt.grid(True)
    plt.savefig("jpmorgan_data_science_project/jpm_adj_close_price.png")
    plt.close()

    plt.figure(figsize=(12, 6))
    sns.histplot(df["Daily_Return"].dropna(), bins=50, kde=True)
    plt.title("Distribution of JPM Daily Returns")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.savefig("jpmorgan_data_science_project/jpm_daily_returns_distribution.png")
    plt.close()

if __name__ == "__main__":
    file_path = "jpmorgan_data_science_project/JPM_historical_data.csv"
    jpm_df = load_data(file_path)
    perform_eda(jpm_df)
    jpm_df_processed = preprocess_data(jpm_df)
    visualize_data(jpm_df_processed)
    jpm_df_processed.to_csv("jpmorgan_data_science_project/JPM_processed_data.csv")
    print("Processed data saved to JPM_processed_data.csv")