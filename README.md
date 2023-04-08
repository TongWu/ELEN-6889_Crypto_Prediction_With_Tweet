# ELEN-6889 Crypto Prediction With Tweet
This repository is about the final project of ELEN 6889 in 23 spring.

## Techniques/Application

### What is the problem you will solve?

The project aims to provide users with real-time cryptocurrency prices and its predicted price trend with related tweets and possible news on the same page. This will help users to make informed decisions quickly regarding the investment. 

### Is there a set of references that motivate this?

The motivation comes from the growing interest in cryptocurrencies investment market and the greater impact of social media sentiment on market trends. Twitter as one of the largest social media and news distributers in the world is the best object to analysis. 

### Do you need to integrate other tools?

Platform for sentiment analysis and machine learning.

## Data/Input

### What data sources will you use?

We will use the twitter API to receive the tweet in real time, and use the API for cryptocurrency to receive the real time cryptocurrency price.

### Will the data be stored and replayed, or pulled in live?

While we want to use a streaming data processing platform which will not require to store the data, the data will still be stored and replayed for the website to show the real time price and the related tweet. The data of tweet and currency price will be stored and linked in the database.

### Do you need to create new connectors to access the data?

We will first use the existing connector like Apache Spark connect to grab data from the APIs. If needed, we will create a custom connector to satisfy special demands.

## Results

### How will you present your results?

Cryptocurrency price trends prediction

### What will you show as a demo?

Perform in a website

## Next Steps

### Will you use any algorithms from class? Will you use any optimizations?

ex: operating reordering, load shedding,......
