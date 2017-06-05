import RPi.GPIO as gpio
import paho.mqtt.client as mqtt
import time
import uuid


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
    client.subscribe("led")


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

client = mqtt.Client(clientid)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username, password)
client.connect(broker, port)
print("mqtt loop start")
client.loop_forever()


