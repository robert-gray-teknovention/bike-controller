import secrets
import network
import time
import urequests
import json
import machine
from bike import run_bike
#from machine import Pin, PWM, Timer
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
server_ip = secrets.IP
port = secrets.PORT
url = server_ip + port + '/apis/status/'
headers = {'Content-Type': 'application/json'}
led = machine.Pin("LED", machine.Pin.OUT)
while not wlan.isconnected():
    led.high()
    wlan.connect(secrets.SSID, secrets.PASSWORD)
    time.sleep(1)  
    led.low()
    time.sleep(3)
while wlan.isconnected():
    try:
        print(wlan.isconnected())
        print(url)
        message = {
            'train': secrets.TRAIN_ID,
            'status': 'POWERED',
            }
        m = json.dumps(message)
        h = json.dumps(headers)
        print(m)
        led = machine.Pin("LED", machine.Pin.OUT)
        led.high()
        r = urequests.post(url, data=m, headers=headers, timeout=1.0)
        print(r.status_code)
        if r.status_code == 201:
            
            led.low()
            run_bike()
            break
            
    except Exception as e:
        print(e)


