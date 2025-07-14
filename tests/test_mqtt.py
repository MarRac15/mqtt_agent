from paho.mqtt import client as mqtt
from dotenv import load_dotenv
import os

load_dotenv()
MQTT_BROKER = os.getenv("MQTT_BROKER")
MQTT_PORT = int(os.getenv("MQTT_PORT", 8900))
MQTT_TOPIC = os.getenv("MQTT_TOPIC")
USER = os.getenv("USER")
API_KEY = os.getenv("API_KEY")

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected!" if rc == 0 else f"Failed: {rc}")
    client.subscribe("#")

def on_message(client, userdata, msg):
    print(f"Message: {msg.topic} → {msg.payload.decode()}")

client = mqtt.Client()
client.username_pw_set(USER, API_KEY)
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT)
client.loop_forever()
