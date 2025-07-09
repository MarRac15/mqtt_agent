from dotenv import load_dotenv
import os

load_dotenv()

def load_config():
    mqtt_config = {
        "broker": os.getenv("MQTT_BROKER"),
        "port": int(os.getenv("MQTT_PORT", 1883)),
        "topic": os.getenv("MQTT_TOPIC"),
        "user": os.getenv("USER"),
        "password": os.getenv("API_KEY")
        #"client_id": os.getenv("MQTT_CLIENT_ID")
    }
    kafka_config = {
        "bootstrap_server": os.getenv("KAFKA_BOOTSTRAP_SERVER"),
        "topic": os.getenv("KAFKA_TOPIC")
    }

    return {"mqtt": mqtt_config, "kafka": kafka_config}