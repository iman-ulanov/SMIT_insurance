import datetime
import json
from collections import deque
from confluent_kafka import Producer
from threading import Lock
import time

producer_config = {
    'bootstrap.servers': 'kafka:9092',
    'client.id': 'insurance-api'
}

producer = Producer(producer_config)

log_queue = deque()
log_lock = Lock()


def send_batch():
    global log_queue
    while log_queue:
        with log_lock:
            log_message = log_queue.popleft()
        producer.produce("action_logs", key=str(log_message['user_id']), value=json.dumps(log_message))
    producer.flush()


def log_to_kafka(user_id: int, action: str, event_time: datetime):
    """Логирование действий через Kafka с использованием батчирования."""
    log_message = {
        "user_id": user_id,
        "action": action,
        "event_time": event_time.strftime("%Y-%m-%d %H:%M:%S")
    }

    with log_lock:
        log_queue.append(log_message)

    if len(log_queue) >= 10:
        send_batch()
    else:
        time.sleep(10)
        send_batch()
