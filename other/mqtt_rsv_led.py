import RPi.GPIO as gpio
import paho.mqtt.client as mqtt
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("estim")


# def on_subscribe(client, userdata, mid, granted_qos):
#     print("Connected with result code "+str(rc))
#     client.subscribe("s")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.payload == b'1':
        gpio.output(20, gpio.LOW)
    else:
        gpio.output(20, gpio.HIGH)


gpio.setmode(gpio.BCM)
gpio.setup(20, gpio.OUT)
gpio.setup(21, gpio.OUT)
gpio.output(20, gpio.HIGH)
gpio.output(21, gpio.HIGH)

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
# mqttc.on_subscribe = o
mqttc.connect("broker.hivemq.com", 1883, 60)
# mqttc.subscribe("estim", 1)
mqttc.loop_forever()
time.sleep(1)

