# data_collection.py
import requests
import yfinance as yf
import pandas as pd
from config import API_KEY_ALPHA_VANTAGE, DEFAULT_SYMBOL, START_DATE, END_DATE, NEWS_QUERY

def collect_stock_data(symbol=DEFAULT_SYMBOL, start=START_DATE, end=END_DATE):
    """Collect stock data for a given ticker and date range."""
    data = yf.download(symbol, start=start, end=end)
    data.to_csv(f"../data/raw/{symbol}_stock_data.csv")
    return data

def collect_news_data(query=NEWS_QUERY):
    """Collect news headlines data from Alpha Vantage News API."""
    url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&keywords={query}&apikey={API_KEY_ALPHA_VANTAGE}"
    response = requests.get(url)
    news_data = response.json()
    headlines = [(item['title'], item['time_published']) for item in news_data.get("feed", [])]
    df = pd.DataFrame(headlines, columns=["headline", "timestamp"])
    df.to_csv(f"../data/raw/{query}_news_data.csv", index=False)
    return df


if __name__ == "__main__":
    collect_stock_data()
    collect_news_data()
