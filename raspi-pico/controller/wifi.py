import secrets
import network
import time
import urequests
import json

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
server_ip = 'http://192.168.0.100'
port = ':9900'
url = server_ip + port + '/apis/status/'
headers = {'Content-Type': 'application/json'}
while not wlan.isconnected():
    wlan.connect(secrets.SSID, secrets.PASSWORD)
    time.sleep(2)

while wlan.isconnected():
    try:
        print(wlan.isconnected())
        print(url)
        message = {
            'train': 1,
            'status': 'POWERED',
            }
        m = json.dumps(message)
        h = json.dumps(headers)
        print(m)
        r = urequests.post(url, data=m, headers=headers)
        print("Hey we just sent a request")
        print(r.status_code)
    except Exception as e:
        print(e)
    time.sleep(100)


