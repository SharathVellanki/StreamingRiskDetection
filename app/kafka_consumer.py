from kafka import KafkaConsumer
import json
from app.model import predict_risk

consumer = KafkaConsumer(
    "risk-input",
    bootstrap_servers='host.docker.internal:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='risk-detector'
)

print("[KafkaConsumer] Listening for messages...")

for message in consumer:
    data = message.value
    features = data.get("features", [])
    
    if len(features) == 30:
        prediction = predict_risk(features)
        label = "RISKY" if prediction == 1 else "SAFE"
        print(f"[KafkaConsumer] Prediction: {label} (raw={prediction})")
    else:
        print(f"[KafkaConsumer] Skipped invalid message: {data}")
