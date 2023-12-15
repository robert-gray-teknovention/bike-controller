#test.py
import bluetooth
from ble_central import BLESimpleCentral
import time
import urequests
import json
import secrets
from wifi import WifiConnector
from lionchief import LionChief
from bike import run_bike
if __name__ == "__main__":
    addr_string = 'FA:28:35:37:B6:54'
    addr = bytes.fromhex(addr_string.replace(':', ''))
    print(addr)
    addr_type = 0

    #ble = bluetooth.BLE()
    chief = LionChief(addr)
    server_ip = secrets.IP
    port = secrets.PORT
    url = server_ip + port + '/apis/status/'
    headers = {'Content-Type': 'application/json'}
    wifi = WifiConnector(secrets.SSID, secrets.PASSWORD)
    time.sleep(1)
    print(secrets.SSID, ' ', secrets.PASSWORD)
    print("Wifi ", wifi.isconnected())
    bike_running = False
    while(1):
        not_found = False
        while not chief.is_connected():
            time.sleep_ms(1000)
            print("We are not connected")
            break
        
        def on_rx(v):
            buf1 = bytearray(v)
            print("RX ")
            for _ in v:
                print(chr(_), end='')
            print("")

        chief._ble_central.on_notify(on_rx)
        
        while chief.is_connected():
            print("We are connected to train")
            with_response=False
            try:
                #v = str(i) + "_"
                
                chief.set_horn(True)
                time.sleep(.5)
                
                chief.set_speed(25)
                time.sleep(2)
                chief.set_horn(False)
                
            except:
                print("TX failed")
            try:
                if not wifi.isconnected() :
                    wifi.connect()
                else:
                    message = {
                        'train': 2,
                        'status': 'RUNNING',
                        }
                    m = json.dumps(message)
                    h = json.dumps(headers)
                    print(m)
                    r = urequests.post(url, data=m, headers=headers)
                    print("Hey we just sent a request")
                    print(r.status_code)
            except Exception as e:
                print(e)
            
            time.sleep_ms(2000 if with_response else 2000)
            run_bike()
                
        chief.scan_connect()
           
            
        print("Disconnected")
        print(" Is the bike running?", bike_running)
        print("Wifi Connected ", wifi.isconnected())
    
        
        