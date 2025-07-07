from paho.mqtt import client as mqtt_client
from config import load_config

def main():
    config = load_config()
    mqtt_config = config["mqtt"]

if __name__ == "__main__":
    main()


