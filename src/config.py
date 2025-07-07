from dotenv import load_dotenv
import os

load_dotenv()

def load_config():
    mqtt_config = {
        "broker": os.getenv("MQTT_BROKER"),
        "port": int(os.getenv("MQTT_PORT", 1883)),
        "topic": os.getenv("MQTT_TOPIC"),
    }

    return {"mqtt": mqtt_config}