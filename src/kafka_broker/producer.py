#kafka prodcuer
from kafka import KafkaProducer
from config import load_config
import ssl
import json


def send_message(producer, message, topic):
    producer.send(topic=topic, value=message).add_errback(on_send_error)

def on_send_error():
    #if cannot send a message then store it somewhere
    pass


def create_producer(kafka_config):
    #kafka_config = config["kafka"]

    #just for development:
    context = ssl.create_default_context()
    context.load_cert_chain(certfile=kafka_config["cert_file"], keyfile=kafka_config["key_file"])
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    producer = KafkaProducer(
        bootstrap_servers = kafka_config["bootstrap_server"],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        security_protocol='SSL',
        ssl_context=context
        )
    return producer

def send_to_kafka(producer, message, config):
        #kafka_config = config["kafka"]
        send_message(producer, message, config["topic"].strip())
        print(f"Sent {message}")
        producer.flush()


#test
# config = load_config()
# kafka_config = config["kafka"]
# producer = create_producer(kafka_config)
# producer.send(kafka_config["topic"].strip(), {'PCSS1': ['2025-07-10T12:30:12Z', 0.0]})
# producer.flush()