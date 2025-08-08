import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

def load_processed_data(file_path):
    """Loads processed data from a CSV file."""
    df = pd.read_csv(file_path, index_col="Date", parse_dates=True)
    return df

def train_and_evaluate_model(df):
    """Trains a linear regression model and evaluates it."""
    # Drop rows with NaN values that might have resulted from feature engineering (e.g., first few MA values)
    df_cleaned = df.dropna()

    # Define features (X) and target (y)
    # Using lagged Adj Close as a simple feature for prediction
    df_cleaned["Adj Close Lag1"] = df_cleaned["Adj Close"].shift(1)
    df_cleaned = df_cleaned.dropna() # Drop NaN from the lagged feature

    X = df_cleaned[["Adj Close Lag1", "Volume", "MA_20", "MA_50"]]
    y = df_cleaned["Adj Close"]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=False) # Time series data, so no shuffle

    # Initialize and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"\n--- Model Evaluation ---")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R-squared: {r2:.2f}")

    # Plot predictions vs actual values
    plt.figure(figsize=(14, 7))
    plt.plot(range(len(y_test)), y_test, label="Actual Adj Close", color="blue")
    plt.plot(range(len(y_test)), y_pred, label="Predicted Adj Close", color="red", linestyle="--")
    plt.title("JPM Adjusted Close Price: Actual vs. Predicted")
    plt.xlabel("Date")
    plt.ylabel("Adjusted Close Price")
    plt.legend()
    plt.grid(True)
    plt.savefig("jpmorgan_data_science_project/jpm_actual_vs_predicted.png")
    plt.close()

    return model, mse, r2

if __name__ == "__main__":
    file_path = "jpmorgan_data_science_project/JPM_processed_data.csv"
    jpm_df_processed = load_processed_data(file_path)
    model, mse, r2 = train_and_evaluate_model(jpm_df_processed)
    print("Modeling complete. Check jpm_actual_vs_predicted.png for visualization.")