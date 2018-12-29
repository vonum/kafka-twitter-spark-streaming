# Twitter streaming with Kafka

Using twitter stream to collect tweets and process them through Kafka.

## Components:
1. Twitter stream
2. Producer to forward tweets to kafka
3. Consumer to process tweets that sent to kafka

## Installation
`pip install -r requirements.txt`

1. Create Twitter API account and get keys for [twitter_config.py](https://github.com/kaantas/kafka-twitter-spark-streaming/blob/master/twitter_config.py)
2. Start Apache Kafka
3. `python producer.py` - Run producer
4. `python consumer.py` - Run consumer
