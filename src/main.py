from config import load_config
from mqtt.client import connect_mqtt


def main():
    config = load_config()
    #mqtt_config = config["mqtt"]

    # kafka_config = config["kafka"]
    # producer = create_producer(config)
    # producer.send(kafka_config["topic"].strip(), {'PCSS1': ['2025-07-10T12:30:12Z', 0.0]})
    # producer.flush()

    client = connect_mqtt(config)
    client.loop_forever()
    

if __name__ == "__main__":
    main()


