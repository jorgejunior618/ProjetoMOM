import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883

sensorPublisher = mqtt.Client()
sensorPublisher.connect(broker, port)

# sensorPublisher = mqtt.Client()
# sensorPublisher.publish(topicos[topico], f"Sensor de {topicos[topico].split("/")[1]}")
