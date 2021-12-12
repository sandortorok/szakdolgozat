import paho.mqtt.client as mqtt
import time
def on_message(client, userdata, message):
    print(message.payload)
mqttBroker = "192.168.10.105"
client = mqtt.Client("Phone")
client.connect(mqttBroker)

client.loop_start()
client.subscribe("testMessage")
client.on_message = on_message



time.sleep(30)
client.loop_stop()
