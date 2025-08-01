from kafka import KafkaConsumer
import json
from textblob import TextBlob
from db import save_tweet
from config import KAFKA_TOPIC, KAFKA_BOOTSTRAP_SERVERS

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

for msg in consumer:
    tweet = msg.value["tweet"]
    blob = TextBlob(tweet)
    sentiment = "positive" if blob.sentiment.polarity > 0 else "negative" if blob.sentiment.polarity < 0 else "neutral"
    save_tweet(tweet, sentiment, blob.sentiment.polarity)
    print(f"Consumed and stored: {tweet} | Sentiment: {sentiment}")
