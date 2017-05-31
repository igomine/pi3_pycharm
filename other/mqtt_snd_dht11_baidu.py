import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import uuid
import sys


# broker = 'swpu-iot.mqtt.iot.gz.baidubce.com'
broker = 'swpu-iot.mqtt.iot.gz.baidubce.com'
port = 1883
username = 'swpu-iot/raspberrypi'
password = 'PLhnSjZDw5z31n2NKI/v8ifr8w+luyE/+p4otPcTx1E='
clientid = 'test'+str(uuid.uuid4())

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("temper")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=21)




client = mqtt.Client(clientid)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username, password)

client.connect(broker, port)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()
time.sleep(2)
print("mqtt loop start")
while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        payload = "Temperature:"+str(result.temperature)
        client.publish("temperature", payload, qos=1, retain=False)
    time.sleep(3)
