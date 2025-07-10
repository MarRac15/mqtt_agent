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
    }

    kafka_config = {
        "bootstrap_server": os.getenv("KAFKA_BOOTSTRAP_SERVER"),
        "topic": os.getenv("KAFKA_TOPIC"),

        #FOR SSL:
        "ca_file": os.getenv("CA_ROOT_LOCATION"),
        "key_file":os.getenv("KEY_LOCATION"),
        "cert_file": os.getenv("CERT_LOCATION"),
        "ssl_pass": os.getenv("SSL_PASSWORD")
    }

    return {"mqtt": mqtt_config, "kafka": kafka_config}