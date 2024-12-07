# CS506 12/10 Final Report

To run the code:

##### TODO

<ol>
<li>Create Makefile, guide on how to run the program</li>
<li>Finish the model</li>
<li>Write the rest of this report</li>

</ol>

# Introduction

In this write up, we will detail our experiments in exploring the iteration between stock movement data, option data, and current events; more specifically, on the creation of a model that, given an aggregate of news headlines from various sources and the calculated sentiments associated with each, will output a series of predictions on the prices of future stock open and close figures. We will step through the engineering decisions from feature extraction to model selection, and explain how each of these components ultimately helped our goal of predicting future stock prices. Finally, we will explain the developments of our findings, and interpret our learnings and results.

(We ultimately were able to do xyz. )

# Data and Methodology

## Data Scraping and APIs

Firstly, we addressed the first goalpost of interpreting current events. Originally, our objective was to obtain a series of current events by writing a program to web-scrape various notable technological journals, including sources like Financial Times, Forbes, New York Times, Reuters. We intended to obtain key headlines related to each of their technology articles (most news-sources have tags that tie each article towards a category), and calculate the sentiment of both the headlines and the bodies of each article. In this way, we could explore how the headlines interact with future stock prices.

However, we ultimately discovered, and decided to focus our efforts on, the Alpha Vantage API. This API provides an endpoint that returns "live and historical news & sentiment data from a large & growing selection of premier news outlets around the world." In using this API, we could obtain, in large quantities, key news articles and their associated sentiment data pre-calculated.

There were a few problems posed by this. Most notably, the news sentiment query only allows for a limit of 1000 news articles and sentiments to be scraped at a time. As such, we had to break down our time frame of one year into multiple different smaller time frames and run a query on each one. However, after we obtained a year's worth of stock data, merging with our obtained stock data, and parsing the data, we have a resulting dataset with 101 rows and 10 columns:

- Adj Close, High, Low, Open: Financial data (adjusted close, high, low, and open prices).
- aggregate_sentiment_mean, aggregate_sentiment_median, aggregate_sentiment_std: Statistical metrics for sentiment aggregation.
- Target, TargetClass: Numerical and categorical targets, respectively.
- TargetNextClose: The predicted next adjusted close price.

(il make charts later)

## Preliminary Analysis on Data

# Model Analysis

# Results
