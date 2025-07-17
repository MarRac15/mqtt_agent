#kafka prodcuer
from utils.saving_messages import save_message
from kafka import KafkaProducer
from kafka.errors import KafkaError
from dotenv import load_dotenv
from pathlib import Path
import time
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



def send_to_kafka(producer, message, retries=3, delay=2):
        attempts = 0
        while attempts < retries:
            try:
                kafka_key = message.get("internalId")
                producer.send(topic=KAFKA_TOPIC, key=kafka_key, value=message)
                print(f"Sent {message}")
                print(f"Set key to {kafka_key}")
                producer.flush()
                return
            except KafkaError as e:
                print(f"Error while sending the message (attempt {attempts+1}/{retries}): {e}")
                attempts+=1
                time.sleep(delay)
        #save the message and retry at the start of the program
        print("All attempts to send a message failed")
        save_message(str(message), 'failed_messages.txt')



# resend the messages if the connection with kafka failed:
def resend_failed_messages(producer):
    if not os.path.exists('failed_messages.txt'):
        return
    try:
        with open('failed_messages.txt', 'r', encoding='utf-8') as file:
            last_message = file.read().strip()
            if not last_message:
                return
            print("Retrying to send failed message...")
            send_to_kafka(producer, last_message)
            open('failed_messages', 'w').close()
    except Exception as e:
        print(f"Error while retrying to send failed message: {e}")
