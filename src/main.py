from config import load_config
from mqtt.client import connect_mqtt

def main():
    config = load_config()
    mqtt_config = config["mqtt"]
    client = connect_mqtt(mqtt_config)
    client.loop_forever()
    #print(f"Received the following message: {client.user_data_get()}")
    #client.user_data_set({"kafka_config": kafka_config})
    

if __name__ == "__main__":
    main()


