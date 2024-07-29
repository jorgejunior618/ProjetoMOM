import paho.mqtt.client as mqtt
from typing import Callable, Any

CallbackOnMessage = Callable[[mqtt.Client, Any, mqtt.MQTTMessage], None]

broker = "localhost"
port = 1883
topic = "test/topic"

def on_message(cli: mqtt.Client, userdata: Any, message: mqtt.MQTTMessage) -> None:
    print(f"topic: {message.topic}")
    print(f"Received message: {message.payload.decode()}")


client = mqtt.Client()
client.on_message = on_message
client.connect(broker, port)
