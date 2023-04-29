import tweepy
from textblob import TextBlob
import csv
import time
import os
import config
import emoji
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


consumer_key = config.API_KEY
consumer_secret= config.API_SECRET
access_token= config.ACCESS_TOKEN
access_token_secret = config.ACCESS_TOKEN_SECRET


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api = tweepy.API(auth)

write_path = True
save_path = "C:/Users/ee527/Desktop/result.csv"



if write_path == True:
    
    try:
        os.remove(save_path)
        #print "File deleted"
    except:
        #print "File was not present already"
        pass

csvFile = open(save_path, 'w', newline = "")

#Use csv writer
csvWriter = csv.writer(csvFile)
#Query(q) ---> AND (surge OR crash OR plunge OR high OR low OR future OR amazing OR good OR bad OR record)
data = tweepy.Cursor(api.search_tweets, q = "bitcoin", until = "2023-04-27 00:00:00", lang = "en", count=100).items(10)
print(data)



#most recent data is fetched first
while True:
  
    tweet = data.next()
    print(tweet.text)
        
    if tweet.user.followers_count > 0: #collecting tweets made by users with min 100k followers
        #i+=1
        # Write a row to the CSV file. I use encode UTF-8
        if write_path == True:
            #emojitotxt = emoji.replace_emoji(tweet.text, replace=" ")
            
            #print(emojitotxt)
            
            user_name = tweet.user.name.encode('utf-8', errors='ignore')
            user_follower = tweet.user.followers_count
            user_date = tweet.created_at
            user_text = tweet.text.encode('utf-8', errors='ignore')
            user_id = tweet.id
        
            
            final_data = [user_name, user_follower, user_date, user_id, user_text]
            
            
            csvWriter.writerow(final_data)
   
        #print("------wrote a tweet-----")

csvFile.close()

