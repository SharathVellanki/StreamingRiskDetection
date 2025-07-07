from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = "risk-input"

def generate_fake_transaction():
    return {
        "features": [round(random.uniform(-5, 5), 4) for _ in range(30)]
    }

if __name__ == "__main__":
    for i in range(20):
        message = generate_fake_transaction()
        producer.send(topic, message)
        print(f"[KafkaProducer] Sent message #{i+1}")
        time.sleep(1)

    producer.flush()
    producer.close()
