from kafka import KafkaConsumer
import redis
import json

r = redis.Redis(host='redis', port=6379, decode_responses=True)

consumer = KafkaConsumer(
    'logs',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='log-consumer-group',
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

print("Consumer started. Listening to 'logs' topic...")

for message in consumer:
    log = message.value
    key = f"log:{log['timestamp']}"
    r.setex(key, 3600, json.dumps(log))  # expire in 1 hour
    print("Stored in Redis:", log)