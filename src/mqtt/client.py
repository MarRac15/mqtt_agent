from paho.mqtt import client as mqtt_client
from utils.saving_messages import save_message
from utils.translator import convert_message
import json

#creates mqtt client
def connect_mqtt(config):

    def on_connect(client, userdata, flags, reason_code):     
        if reason_code == 0:
            print("Connected to MQTT Broker!")
            client.subscribe(config["topic"])
        else:
            print("Failed to connect, return code %d\n", reason_code)
            

    def on_message(client, userdata, msg):
        msg_dict = json.loads((msg.payload))
        print(msg_dict)
        message_content = msg_dict['uplink_message']['decoded_payload']['bytes']
        print(message_content)
        
        clean_message = message_content.replace('\\', '')
        #translation to kafka format:
        convert_message(clean_message)
        #saves messages to a json file:
        save_message(clean_message)

    client = mqtt_client.Client()
    client.username_pw_set(config["user"], config["password"])
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(config["broker"], config["port"])
    

    return client


