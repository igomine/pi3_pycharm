import RPi.GPIO as gpio
import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("swpu-iot")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(str(msg.payload))


gpio.setmode(gpio.BCM)
gpio.setup(20, gpio.OUT)
gpio.setup(21, gpio.OUT)
gpio.output(20, gpio.HIGH)
gpio.output(21, gpio.HIGH)

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
# mqttc.on_subscribe = o
mqttc.connect("broker.mqttdashboard.com", 1883, 60)
# mqttc.subscribe("estim", 1)
mqttc.loop_forever()
time.sleep(1)

