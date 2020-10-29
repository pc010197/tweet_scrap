import sys
import tweepy
import private
import datetime
import time

auth = tweepy.OAuthHandler(private.TWITTER_API_KEY,private.TWITTER_APP_SECRET)

auth.set_access_token(private.TWITTER_KEY,private.TWITTER_SECRET)
api= tweepy.API(auth)

def get_tweets(api,username):
    page =1 
    end=False

    while True:
        tweets = api.user_timeline(username, page=page)

        for tweet in tweets:
            if (datetime.datetime.now()  - tweet.created_at).day < 2:
                print(tweet.text.encode("utf"))

            else:
                end =True
                return
            if not end:
                page + 1
                time.sleep(500)

get_tweets(api,"")# get_tweets(api,username)