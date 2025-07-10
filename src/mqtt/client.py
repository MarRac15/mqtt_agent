from paho.mqtt import client as mqtt_client
from utils.saving_messages import save_message
from utils.translator import convert_message
from kafka_broker.producer import create_producer, send_to_kafka
import json

#creates mqtt client
def connect_mqtt(config):

    mqtt_config = config["mqtt"]
    kafka_config = config["kafka"]

    def on_connect(client, userdata, flags, reason_code):     
        if reason_code == 0:
            print("Connected to MQTT Broker!")
            client.subscribe("#")
        else:
            print("Failed to connect, return code %d\n", reason_code)
            

    def on_message(client, userdata, msg):
        msg_dict = json.loads((msg.payload))
        message_content = msg_dict['uplink_message']['decoded_payload']['bytes']
        print(message_content)
        
        clean_message = message_content.replace('\\', '')
        #translation to kafka format:
        kafka_message = convert_message(clean_message)
        #saves messages to a json file:
        save_message(str(kafka_message))

        #send to kafka:
        send_to_kafka(kafka_producer, kafka_message, kafka_config)

    client = mqtt_client.Client()
    kafka_producer = create_producer(kafka_config)
    client.username_pw_set(mqtt_config["user"], mqtt_config["password"])
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(mqtt_config["broker"], mqtt_config["port"])
    

    return client


