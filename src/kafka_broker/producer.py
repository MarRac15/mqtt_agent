#kafka prodcuer
from kafka import KafkaProducer
from config import load_config
import ssl
import json


def send_message(producer, message, topic):
    producer.send(topic=topic, value=message) #.add_errback(on_send_error)

def on_send_error():
    print(f"Failed to send a message")
    # if the connection to kafka failed then read the last message from msg_data.txt
    # and resend it
    with open('msg_data.txt', 'r', encoding='utf-8') as file:
         for line in file:
              pass
         last_message = line
    return last_message

def create_producer(kafka_config):

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
        send_message(producer, message, config["topic"].strip())
        print(f"Sent {message}")
        producer.flush()

