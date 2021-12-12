import paho.mqtt.client as mqtt
import time
from random import uniform, randrange

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature inside")
client.connect(mqttBroker)

randnumber = uniform(10, 20)
client.publish("TEMPERATURE", randnumber)
print("published " + str(randnumber)+ " to topic TEMPERATURE")
