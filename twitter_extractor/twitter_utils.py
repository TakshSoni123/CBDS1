from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import re,time
from twitter_extractor import twitter_credentials
import pandas as pd
import numpy as np
import sys

class TwitterListener(StreamListener):
  # Listener class to print tweets
  def __init__(self, tweet_file,time_limit = 60):
    self.start_time = time.time()
    self.limit = time_limit
    self.tweet_file=open(tweet_file,'a')

  def on_data(self,data):
    if (time.time() - self.start_time) < self.limit:
      try:
        if data.find('created_at')!=-1:
          # print(data)
          self.tweet_file.write(data+'\n')
      except BaseException as e:
        print('Error: {}'.format(e))
    else:
      print('exiting')
      return False
    return True

  def on_error(self,status):
    if status == 420:
      # If rate limit exceeds, cancel tweet extraction.
      return False
    print(status)


class TwitterAuthenticator():

  def authenticate_twitter(self):
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
    return auth


class TwitterStreamer():
  # Streaming and processing live tweets
  def __init__(self):
    self.twitter_auth=TwitterAuthenticator()

  def stream_tweets(self, tweet_file,time_limit, hash_tag_list=["a", "the", "i", "you", "u"]):
    # Authentication and API connection
    listener = TwitterListener(tweet_file,time_limit)
    auth=self.twitter_auth.authenticate_twitter()
    stream = Stream(auth,listener)
    # stream.sample()
    stream.filter(track=hash_tag_list,languages = ["en"])


class TweetAnalyser():
  # Analysing and Categorizing content from tweets
  def clean_tweet(self, tweet):
    return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+\/\/\S+)', " ", tweet).split())

  def tweets_to_df(self, tweets):
    df = pd.DataFrame()

    df['userid'] = np.array([tweet['user']['id'] for tweet in tweets])
    df['username'] = np.array([tweet['user']['name'] for tweet in tweets])
    df['date'] = np.array([tweet['created_at'] for tweet in tweets])
    df['tweet'] = np.array([tweet['text'] for tweet in tweets])

    return df

  # def json_to_df
