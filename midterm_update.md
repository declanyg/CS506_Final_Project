# CS506 11/15 Midterm Report

##### to be added to readme once written :)

In the past month, we have analyzed and established a plan to explore stock prices in the technology field by exploring the iteration between stock movement data, option data, and current events.

We've done preliminary analysis on some of the sources we can use to actually construct our model. Of note, not all of the available news sources will be able to provide us a sufficient amount of data to use in training. While we intend to use an aggregate of multiple News APIs to construct our final training set, for our current intermediary testing, we have ruled out some sources of data.

We have decided on predicting a precise ticker: **QQQ**. This will allow us to precisely train on the tech subset of the news headlines, simplifying the training process, as \_\_\_ tracks specifically technology companies' prices.

To obtain stock ticker numbers from market data in the past year, we use the Yahoo Finance API. This allows us to obtain all prices from **QQQ** in the past year.

![alt text](./plots/QQQ_price.png)
