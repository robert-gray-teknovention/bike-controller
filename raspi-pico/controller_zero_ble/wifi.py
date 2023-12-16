import secrets
import network
import time
import urequests
import json

class WifiConnector():
    
    def __init__(self, ssid, password):
        self._wlan = network.WLAN(network.STA_IF)
        self._wlan.active(True)
        self._ssid = ssid
        self._password = password
        print (self._ssid)
        
    def connect(self, attempts=5, timeout=1):
        if self._wlan.isconnected():
            print("We are already connected")
            return True
        for i in range(1, attempts):
            print('Connecting to ', self._ssid, ' ', self._password)
            self._wlan.connect(self._ssid, self._password)
            time.sleep(2)
            if self._wlan.isconnected():
                return True
            else:
                time.sleep(timeout)
                print ("We are going to retry the connection. Attempt ", str(i), " of ", str(attempts))
        print("We were unable to connect. Please check ssid and password")
        return False
    
    def disconnect(self):
        self._wlan.disconnect()
        print("We disconnected from ", self._ssid)
    
    def isconnected(self):
        return self._wlan.isconnected()
        
    
'''
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
server_ip = 'http://10.10.10.110'
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
'''

