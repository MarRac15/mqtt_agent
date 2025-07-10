from config import load_config
from mqtt.client import connect_mqtt


def main():
    config = load_config()
    client = connect_mqtt(config)
    client.loop_forever()
   

if __name__ == "__main__":
    main()


