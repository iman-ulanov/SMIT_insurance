from kafka import KafkaConsumer
import json

KAFKA_SERVER = 'localhost:9092'
TOPIC = 'action_logs'
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=[KAFKA_SERVER],
    group_id='action-logs-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print(f"Listening for messages on topic '{TOPIC}'...")

for message in consumer:
    print(f"Received message: {message.value}")
