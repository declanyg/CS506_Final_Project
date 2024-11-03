from textblob import TextBlob
import pandas as pd
from config import NEWS_QUERY

def get_sentiment(headline):
    """Calculate sentiment polarity of a headline."""
    blob = TextBlob(headline)
    return blob.sentiment.polarity

def analyze_headline_sentiments(input_file=None, output_file=None):
    """Analyze sentiment for each headline in a CSV file."""
    # Set default file paths if not provided
    if input_file is None:
        input_file = f"../data/raw/{NEWS_QUERY}_news_data.csv"
    if output_file is None:
        output_file = f"../data/sentiment/{NEWS_QUERY}_news_sentiment.csv"
    
    # Read the input CSV file
    df = pd.read_csv(input_file)
    
    # Calculate sentiment for each headline
    df['sentiment'] = df['headline'].apply(get_sentiment)

    # Save the results to the output CSV file
    df.to_csv(output_file, index=False)
    return df

if __name__ == "__main__":
    analyze_headline_sentiments()
