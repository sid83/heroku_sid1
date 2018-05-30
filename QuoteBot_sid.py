# Dependencies
import tweepy
import time
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret

# Quotes to Tweet
quotes=["This is tweet#1","This is tweet#2","This is tweet#3"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Create function for tweeting
def tweet_func(tweetnumber):
    api.update_status(quotes[tweetnumber])
    print(f"tweet {tweetnumber} is a success")

counter=0

# Set timer to run every minute
while(True):
    tweet_func(counter)
    # print(quotes[counter])
    # wait for 10 sec
    time.sleep(3)
    counter+=1
    if counter>2:
        break
