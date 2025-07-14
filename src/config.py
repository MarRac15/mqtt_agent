from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

MQTT_BROKER = os.getenv("MQTT_BROKER")
MQTT_PORT = int(os.getenv("MQTT_PORT", 8900))
MQTT_TOPIC = os.getenv("MQTT_TOPIC")
USER = os.getenv("USER")
API_KEY = os.getenv("API_KEY")

#kafka config:
KAFKA_BOOTSTRAP_SERVER = os.getenv("KAFKA_BOOTSTRAP_SERVER")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

#FOR SSL (kafka):
CA_ROOT_LOCATION = os.getenv("CA_ROOT_LOCATION")
CERT_LOCATION = str(Path(os.getenv("CERT_LOCATION")).resolve())
KEY_LOCATION = str(Path(os.getenv("KEY_LOCATION")).resolve())
SSL_PASSWORD = os.getenv("SSL_PASSWORD")

# def load_config():
#     mqtt_config = {
#         "broker": os.getenv("MQTT_BROKER"),
#         "port": int(os.getenv("MQTT_PORT", 8900)),
#         "topic": os.getenv("MQTT_TOPIC"),
#         "user": os.getenv("USER"),
#         "password": os.getenv("API_KEY")
#     }

#     kafka_config = {
#         "bootstrap_server": os.getenv("KAFKA_BOOTSTRAP_SERVER"),
#         "topic": os.getenv("KAFKA_TOPIC"),

#         #FOR SSL:
#         "ca_file": os.getenv("CA_ROOT_LOCATION"),
#         "key_file":os.getenv("KEY_LOCATION"),
#         "cert_file": os.getenv("CERT_LOCATION"),
#         "ssl_pass": os.getenv("SSL_PASSWORD")
#     }

#     return {"mqtt": mqtt_config, "kafka": kafka_config}