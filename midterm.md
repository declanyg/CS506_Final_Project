# CS506 11/15 Midterm Report

[Video Link](https://youtu.be/w82ezjrV92A?si=dJJOjJ22cIAZvd9n)

In the past month, we have analyzed and established a plan to explore stock prices in the technology field by exploring the iteration between stock movement data, option data, and current events.

We've done preliminary analysis on some of the sources we can use to actually construct our model. Of note, not all of the available news sources will be able to provide us a sufficient amount of data to use in training. While we intend to use an aggregate of multiple News APIs to construct our final training set, for our current intermediary testing, we have ruled out some sources of data.

We have decided on predicting a precise ticker: **QQQ**. This will allow us to precisely train on the tech subset of the news headlines, simplifying the training process, as QQQ tracks specifically technology companies' prices.

### Stock Market Data

We have decided on predicting a precise ticker: **QQQ**. This will allow us to precisely train on the tech subset of the news headlines, simplifying the training process, as **QQQ** tracks the Nasdaq-100 Index that includes the 100 largest non-financial companies listed on NasDaq. 50% of the stocks on Nasdaq are classifed as tech stocks according to US News.

To obtain stock ticker numbers from market data in the past year, we use the Yahoo Finance API. This allows us to obtain all prices from **QQQ** in the past year. Although the amount of data within one year may be considered quite little, it should be sufficent to determine patterns. Below is a plotted image of the stock data over time

![Market Data](./plots/QQQ_price.png)

### Financial Headline Data

For now, we focus our efforts on processing data from Alpha Vantage API. Although each call gives us a large quantity of usable data, including sentiment analysis and relevancy of each given news article and headline, there were a few problems posed by this. Most notably, the news sentiment query only allows for a limit of 1000 news articles and sentiments to be scraped at a time. As such, we had to break down our time frame of one year into multiple different smaller time frames and run a query on each one. To maximize the potential amount of scrapable data, we decided to break it into time frames of 6 days each, since 366 is divisible by 6. However, this led to the issue of being rate limited by the free API which restricts it to a limit of 25 API requests per day. Thus, currently, the amount of data we scraped is through the use of bi-weekly time frames. As for the specific columns of data we decided to keep, they are as follows:

- title
- url
- time_published
- source
- overall_sentiment_score
- overall_sentiment_label
- ticker_sentiment
  Overall sentiment_score x and label are defined as x <= -0.35: Bearish; -0.35 < x <= -0.15: Somewhat-Bearish; -0.15 < x < 0.15: Neutral; 0.15 <= x < 0.35: Somewhat_Bullish; x >= 0.35: Bullish , according to the Alpha Vantage API.

To better understand the financial headline data, and to decide on how to model the data, multiple plots were made.

The distribution of sentiment scores by source is as follows:
![Financial Data](./plots/Average_Overall_Sentiment_Score_by_Source.png)

The distribution of sentiment scores by label is as follows:
![Financial Data](./plots/Distribution_of_Overall_Sentiment_Labels.png)

These models show that the distribution of the sentiment data is rather skewed, with only about 0.3% of the articles being classified as bearish. Thus, data sampling techniques should be used to rebalance the data.

### Preliminary Results

To start, we decided to fit out data to a linear regression model. The biggest challenge for this was figuring out how to use our collected data to train the model. Eventually, we decided on training the preliminary model on the average sentiments from specific news source on each unique day. As such, each source was one hot encoded, then assigned the average sentiments from each news source published on that day. The model can be seen below:

![Linear Regression Model](./plots/LinearRegressionPreliminaryPlot.png)

This model has a MSE of about 6784 and thus can be considered to be not that good with predicting the data (average difference in predicted and actual price is about $82). Hence, we will most likely change our model to a neural network or decision tree in the latter half of this project.

# CS506_Final_Project

CS506_Final_Project (UPDATE 1)

Description of the project

- This project is to explore stock prices in the tech field by exploring the iteration between stock movement data, options data, and current events.
- The goal is to beat a simple buy-sell strategy by modeling the peaks of the stock price over a period of time. The model will be considered a success if the average predicted price difference is within a margin of error.
- The following data will be collected:
  - Stock movement data
  - Options data
  - Current events (headlines)
- The data will be collected through the use of both scraping and publically available APIs. Specifically that of the Yahoo Finance API Polygon.io for stock data, and Alpha Vantage and AP News API for news sentiment analysis. This list may be further improved upon during the actual development process.
- To account for the biases that may be present in news article headlines, headliens from multiple different news sources will be collected to ensure that there is a diverse set of perspectives present.
- The model will be modelled with either multi-linear regression, multivariate polynomial regression, or a neural network. It will use scalars and vectorized strings for training to account for the stock data and news headlines respectively.
  - Multi-linear Regression: Each feature (stock price, sentiment from given news sources) is a independent variable that will be against the dependent variable of time
  - Multivariate Polynomial Regression: Same as mulit-linear regression but uses polynomial weightings in case the model doesn't follow a strictly linear trend
  - Neural Network/Convolutional Neural Network: A more powerful model that automatically finds weightings based on layers of perceptrons through the use of backpropagation. The inputs will be the stated features above (stock price, sentiment from given news sources) while the output is the stock price. This will allow for more prcesise decision boundaries.
- It will be visualized by charting price against time and comparing our predicted price vs the actual price over a time period
- The data will follow a standard train test val split, 80-10-10, within the past year (Sep 2023 to Sep 2024).
