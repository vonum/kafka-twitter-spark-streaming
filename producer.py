from pykafka import KafkaClient

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_config
import json

class StreamListener(tweepy.StreamListener):
  def __init__(self, producer):
    self.producer = producer

  def on_status(self, status):
    print(status.text)
    return True

  def on_data(self, data):
    print(data)
    self.producer.produce(bytes(data, "ascii"))
    return True

  def on_error(self, status):
    print(status)
    return True

#TWITTER API CONFIGURATIONS
consumer_key = twitter_config.consumer_key
consumer_secret = twitter_config.consumer_secret
access_token = twitter_config.access_token
access_secret = twitter_config.access_secret

#TWITTER API AUTH
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

client = KafkaClient(hosts="127.0.0.1:9092")
topic = client.topics["twitter.ai.test"]
producer = topic.get_sync_producer()

#Twitter Stream Config
twitter_stream = Stream(auth, StreamListener(producer))

#Produce Data that has ai hashtag (Tweets)
twitter_stream.filter(track=["ai"])
