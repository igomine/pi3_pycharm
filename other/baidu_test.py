import paho.mqtt.client as mqtt
import sys
import uuid

broker = 'swpu-iot.mqtt.iot.gz.baidubce.com'
port = 1883
username = 'iotfreetest/thing01'
password = 'njsY3ZXCKmdijQZpAfCN2CnLfNFS0aT1TugrlTRVS28='
clientid = 'test_mqtt_python_' + str(uuid.uuid4())
topic = 'demoTopic'

def on_connect(client, userdata, rc):
    print('Connected. Client id is: ' + clientid)
    client.subscribe(topic)
    print('Subscribed to topic: ' + topic)

    client.publish(topic, 'Message from Baidu IoT demo')
    print('MQTT message published.')

def on_message(client, userdata, msg):
    msg = str(msg.payload, 'utf-8')
    print('MQTT message received: ' + msg)
    if msg == 'exit':
        sys.exit()

client = mqtt.Client(clientid)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username, password)

print('Connecting to broker: ' + broker)
client.connect(broker, port)

client.loop_forever()