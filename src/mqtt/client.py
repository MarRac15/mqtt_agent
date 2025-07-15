from paho.mqtt import client as mqtt_client
import os
from dotenv import load_dotenv
from utils.saving_messages import save_message
from utils.translator import convert_message
from kafka_broker.producer import create_producer, send_to_kafka, resend_failed_messages
import json


load_dotenv(override=True)

MQTT_BROKER = os.getenv("MQTT_BROKER")
MQTT_PORT = int(os.getenv("MQTT_PORT", 8900))
MQTT_TOPIC = os.getenv("MQTT_TOPIC")
USER = os.getenv("USER")
API_KEY = os.getenv("API_KEY")

#creates mqtt client
def connect_mqtt():

    def on_connect(client, userdata, flags, reason_code, properties=None):     
        if reason_code == 0:
            print("Connected to MQTT Broker!")
            result, mid = client.subscribe(MQTT_TOPIC)
            print(f"Subscribed to topic '{MQTT_TOPIC}' with result code {result}")
        else:
            print("Failed to connect, return code %d\n", reason_code)
            

    def on_message(client, userdata, message):
        print("Message received!")
        msg_dict = json.loads((message.payload))
        message_content = msg_dict['uplink_message']['decoded_payload']['bytes']
        print(message_content)
        
        clean_message = message_content.replace('\\', '')
        #translation to kafka format:
        kafka_message = convert_message(clean_message)
        if kafka_message:
            #saves messages to a file:
            save_message(str(kafka_message), 'msg_data.txt')
            #send it to kafka:
            if kafka_producer:
                send_to_kafka(kafka_producer, kafka_message)
            else:
                print("Kafka producer won't be created, please check you /certs directory")
        else:
            print("Received an empty message!")


    client = mqtt_client.Client()
    kafka_producer = create_producer()
    resend_failed_messages(kafka_producer)
    client.username_pw_set(USER, API_KEY)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER, MQTT_PORT, keepalive=600)
    

    return client


