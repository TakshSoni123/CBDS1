from twitter_extractor.twitter_utils import TweetAnalyser,TwitterStreamer
import atexit
import json,os


tweet_file = os.path.join(os.getcwd(),'twitter_extractor/tweets.json')


def create_dataframe():
    analyser = TweetAnalyser()
    tweets = []

    with open(tweet_file,'r') as f:
        for line in f.readlines():
            if line!='\n':
                tweet = json.loads(line)
                tweets.append(tweet)
        # print(analyser.tweets_to_df([tweet]))
    df = analyser.tweets_to_df(tweets)
    print(df.shape)
    return df


def run():
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(tweet_file=tweet_file,time_limit=1)

    return create_dataframe()
