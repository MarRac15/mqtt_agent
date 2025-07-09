#kafka prodcuer
from kafka import KafkaProducer
import time
import json
from config import load_config


def send_message(producer, message, topic):
    producer.send(topic=topic, value=message).add_errback(on_send_error)

def on_send_error():
    #if cannot send a message then store it somewhere
    pass


def start_producer(max_buffer_size=1024*1024):
    config = load_config()
    kafka_config = config["kafka"]

    #pobierz przetlumaczone wiadomosci z mqtt (z cache/pliku):
    messages = []


    producer = KafkaProducer(
        bootstrap_servers = kafka_config["bootstrap_server"],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        security_protocol='SSL',
        ssl_cafile='',ssl_certfile='',
        ssl_keyfile='',ssl_password=''
        )
    
    buffer = []
    buffer_size = 0


    while buffer_size <= max_buffer_size:
        for msg in messages:
            buffer.append(msg)
            buffer+=len(msg.encode('utf-8'))
            send_message(producer, msg, kafka_config["topic"])
            print(f"Sent {msg}")

    