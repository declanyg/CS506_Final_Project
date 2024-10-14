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
