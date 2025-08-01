from kafka import KafkaProducer
from faker import Faker
import json
import time
from config import KAFKA_TOPIC, KAFKA_BOOTSTRAP_SERVERS

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

if __name__ == "__main__":
    while True:
        tweet = fake.sentence()
        producer.send(KAFKA_TOPIC, {"tweet": tweet})
        print(f"Produced: {tweet}")
        time.sleep(2)
