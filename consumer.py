from pykafka import KafkaClient
import json

client = KafkaClient(hosts="127.0.0.1:9092")
topic = client.topics["twitter.ai.test"]
consumer = topic.get_simple_consumer()

for message in consumer:
  if message is not None:
    tweet = json.loads(message.value)
    print(tweet["text"])
