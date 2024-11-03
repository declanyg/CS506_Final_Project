import pandas as pd
from config import DEFAULT_SYMBOL, NEWS_QUERY

def calculate_daily_returns(df):
    """Calculate daily returns for stock price data."""
    df['Daily_Returns'] = df['Close'].pct_change()
    return df

def calculate_moving_average(df, window=20):
    """Calculate moving average for a given window size."""
    df[f'MA_{window}'] = df['Close'].rolling(window=window).mean()
    return df

def prepare_features(stock_file=None, sentiment_file=None, output_file=None):
    """Prepare final feature dataset by merging stock and sentiment data."""
    # Set default file paths if not provided
    if stock_file is None:
        stock_file = f"../data/raw/{DEFAULT_SYMBOL}_stock_data.csv"
    if sentiment_file is None:
        sentiment_file = f"../data/sentiment/{NEWS_QUERY}_news_sentiment.csv"
    if output_file is None:
        output_file = f"../data/processed/{DEFAULT_SYMBOL}_features.csv"
    
    # Load the stock data, specifying the correct header
    stock_df = pd.read_csv(stock_file, header=2)  # Use the third row (index 2) as the header

    # Strip whitespace from column names
    stock_df.columns = stock_df.columns.str.strip()

    # Rename columns for consistency
    stock_df.rename(columns={
        'Date': 'timestamp',
        'Unnamed: 1': 'Adj_close',
        'Unnamed: 2': 'Close',
        'Unnamed: 3': 'High',
        'Unnamed: 4': 'Low',
        'Unnamed: 5': 'Open',
        'Unnamed: 6': 'Volume'
    }, inplace=True)
    
    print("Initial Stock Data:", stock_df.head())
    
    # Convert the timestamp to UTC
    stock_df['timestamp'] = pd.to_datetime(stock_df['timestamp']).dt.tz_convert('UTC')

    # Load the sentiment data
    sentiment_df = pd.read_csv(sentiment_file)
    sentiment_df.rename(columns={'Date': 'timestamp'}, inplace=True)

    # Convert the timestamp to datetime and localize to UTC
    sentiment_df['timestamp'] = pd.to_datetime(sentiment_df['timestamp'])
    sentiment_df['timestamp'] = sentiment_df['timestamp'].dt.tz_localize('UTC')

    # Merge DataFrames on 'timestamp'
    df = pd.merge(stock_df, sentiment_df, how='left', on='timestamp')
    print("Initial Stock Data:", df.head())
    # Calculate daily returns and moving averages
    df = calculate_daily_returns(df)
    df = calculate_moving_average(df)
    
    # Save the final DataFrame to CSV
    df.to_csv(output_file, index=False)
    
    return df

if __name__ == "__main__":
    prepare_features()
