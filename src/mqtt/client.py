from paho.mqtt import client as mqtt_client
from utils.saving_messages import save_message
import json

#creates mqtt client
def connect_mqtt(config):

    Status = {}

    def on_connect(client, userdata, flags, reason_code):    
        #client.subscribe('#')   
        if reason_code == 0:
            print("Connected to MQTT Broker!")
            client.subscribe(config["topic"])
        else:
            print("Failed to connect, return code %d\n", reason_code)
            

    def on_message(client, userdata, msg):

        print(msg.topic+" "+str(msg.payload))
        msg_dict = json.loads((msg.payload))
        Status.update(msg_dict)
        #saves messages to a file:
        #save_message(Status)
        #WIP
        #...translation here...

    client = mqtt_client.Client()
    client.username_pw_set(config["user"], config["password"])
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(config["broker"], config["port"])
    

    return client


