import network
import time
from umqtt.simple import MQTTClient
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("TEKNOVENTION", "flyingcolors")
time.sleep(2)
print(wlan.isconnected())
mqtt_server = 'mqtt.teknovention.com'
client_id = 'raspipico'
topic_pub = b'test'
topic_msg = b'hello from pico'
user = 'rgray'
pwd = 'Aliquippa412'
port = 8883

def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, user=user, password=pwd, port=port, keepalive=3600, ssl=True, ssl_params={'cert': '/etc/ssl/certs/'})
    client.connect()
    print('Connected to %s MQTT Broker.'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnect...')
    time.sleep(5)

try:
    client = mqtt_connect()
    
    
except OSError as e:
    print(e)
    reconnect()

while True:
    client.publish(topic_pub, topic_msg)
    print("We are publishing!")
    time.sleep(5)



