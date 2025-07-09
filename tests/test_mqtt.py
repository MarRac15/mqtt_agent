from paho.mqtt import client as mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected!" if rc == 0 else f"Failed: {rc}")
    client.subscribe("#")

def on_message(client, userdata, msg):
    print(f">>> Message: {msg.topic} → {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("eu1.cloud.thethings.network", 1883)
client.loop_forever()
