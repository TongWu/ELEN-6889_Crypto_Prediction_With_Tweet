import tweepy
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os
import csv
import config
from pyspark import SparkConf, SparkContext
from pyspark.sql.functions import regexp_replace
import pyspark
import emoji
from pyspark.sql import SparkSession
# to directly solve "Python worker failed to connect back" environment problem
import findspark
findspark.init()



# Create a SparkSession
spark = SparkSession.builder.appName("TwitterData").getOrCreate()

# Set up Twitter API credentials
consumer_key = config.API_KEY
consumer_secret= config.API_SECRET
access_token= config.ACCESS_TOKEN
access_token_secret = config.ACCESS_TOKEN_SECRET

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)


# Query Twitter API for tweets
data = tweepy.Cursor(api.search_tweets, q="bitcoin", until="2023-04-28 00:00:00", lang="en", count=1).items(10)

# Create an empty list to store the processed data
processed_data_list = []

while True:
    try:
        tweet = data.next()
            
        user_date = tweet.created_at
        
        user_text = emoji.replace_emoji(tweet.text, replace="")

        final_data = [user_date, user_text]   
            
        processed_data_list.append(final_data)
      
    except StopIteration:
        break

# Create a DataFrame from the processed data list
df = spark.createDataFrame(processed_data_list, ["date", "text"])

# start PySpark transform #####################################################################

# remove mention 
cleaned_df = df.withColumn("text", regexp_replace('text', "@\s*[A-Za-z0-9_]+", ''))
cleaned_df = cleaned_df.withColumn("text", regexp_replace("text", "#\s*[A-Za-z0-9_]+", ""))
# remove retweet
cleaned_df = cleaned_df.withColumn("text", regexp_replace('text', "RT : ", ''))

# remove links
cleaned_df = cleaned_df.withColumn('text', regexp_replace('text', r"http\S+", ''))
cleaned_df = cleaned_df.withColumn('text', regexp_replace('text', r"www.\S+", ''))

# remove next line
cleaned_df = cleaned_df.withColumn("text", regexp_replace("text", r"\n", ""))


cleaned_df = cleaned_df.withColumn('text', regexp_replace('text', '\s+', ' '))



# result = cleaned_df.select("text").show()


# get data
final = cleaned_df.collect()


# start writing data into csv

# open the file in the write mode
# with open("C:\\Users\\ee527\\Desktop\\twitter.csv", 'w', newline='') as f:
#     # create the csv writer
#     writer = csv.writer(f)
    
#     for row in final:
#         print(" ")
#         print(row["text"])     

#         writer.writerow(row)

# Stop the SparkSession
spark.stop()
