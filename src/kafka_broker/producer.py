#kafka prodcuer
from kafka import KafkaProducer
from dotenv import load_dotenv
from pathlib import Path
import os
import ssl
import json



load_dotenv(override=True)

KEY_LOCATION = os.getenv("KEY_LOCATION")
CERT_LOCATION = os.getenv("CERT_LOCATION")
KAFKA_BOOTSTRAP_SERVER = os.getenv("KAFKA_BOOTSTRAP_SERVER")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")
CERT_LOCATION = str(Path(CERT_LOCATION).resolve())
KEY_LOCATION = str(Path(KEY_LOCATION).resolve())


def on_send_error():
    print(f"Failed to send a message")
    # if the connection to kafka failed then read the last message from msg_data.txt
    # and resend it
    with open('msg_data.txt', 'r', encoding='utf-8') as file:
         for line in file:
              pass
         last_message = line
    return last_message

def create_producer():
    if not os.path.exists(CERT_LOCATION) or not os.path.exists(KEY_LOCATION):
         print("Certificate or key file don't exist, check your path.")
         return None
    
    #without CA!
    context = ssl.create_default_context()
    context.load_cert_chain(certfile=CERT_LOCATION, keyfile=KEY_LOCATION)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    producer = KafkaProducer(
        bootstrap_servers = KAFKA_BOOTSTRAP_SERVER,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        key_serializer=lambda k: k.encode('utf-8') if k else None,
        security_protocol='SSL',
        ssl_context=context
        )
    return producer

def send_to_kafka(producer, message):
        kafka_key = message.get("ID")
        producer.send(topic=KAFKA_TOPIC, key=kafka_key, value=message)
        print(f"Sent {message}")
        print(f"Set key to {kafka_key}")
        producer.flush()

