from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

LOG_LEVELS = ["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"]

def generate_log():
    return {
        "level": random.choice(LOG_LEVELS),
        "message": f"Simulated log message {random.randint(1000, 9999)}",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    topic = 'logs'
    print(f"Producing logs to topic: {topic}")
    while True:
        log = generate_log()
        producer.send(topic, log)
        print("Sent:", log)
        time.sleep(1)