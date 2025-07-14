from mqtt.client import connect_mqtt


def main():
    print("App is running")
    client = connect_mqtt()
    client.loop_forever()
   

if __name__ == "__main__":
    main()


