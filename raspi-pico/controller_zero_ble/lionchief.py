import time
import bluetooth
from ble_central import BLESimpleCentral
UUID25 = "08590f7e-db05-467e-8757-72f6faeb13d4"
class LionChief:
    
    def __init__(self, mac, **kwargs):
        if not mac:
            raise "LionChief constructor needs mac address"
        ble = bluetooth.BLE()
        self._ble_central = BLESimpleCentral(ble)
        self._ble_central.addr = mac
        self._ble_central.addr_type = 0
        
    def on_scan(self, addr_type, addr, name):
        if addr_type is not None:
            print("Found peripheral:", addr_type, addr, name)
            self._ble_central.connect()
        else:
            #nonlocal not_found
            #not_found = True
            print("No peripheral found.")
            
    def scan_connect(self):
        self._ble_central.scan(callback=self.on_scan)
    
    def is_connected(self):
        return self._ble_central.is_connected()
        
    def _send_cmd(self, values, with_response):
        checksum = 256
        for v in values:
            checksum -= v;
        while checksum<0:
            checksum+=256
        values.insert(0,0)
        values.append(checksum)
        print("Command values ", str(values), ' bytes: ', bytes(values))
        #self._device.char_write(UUID25, bytes(values), wait_for_response=False);
        self._ble_central.write(bytes(values), with_response)
    
    def set_horn(self, on):
        self._send_cmd([0x48, 1 if on else 0], with_response=False)

    def set_bell(self, on):
        self._send_cmd([0x47, 1 if on else 0], with_response=False)

    def set_bell_pitch(self, pitch):
        pitches = [0xfe, 0xff, 0, 1, 2]
        if pitch<0 or pitch >=len(pitches):
            raise "Bell pitch should be between 0 and "+pitch
        self._send_cmd([0x44, 0x02, 0x0e, pitches[pitch]], with_response=False);

    def speak(self):
        self._send_cmd([0x4d, 3, 0], with_response=False)

    def set_speed(self, speed):
        self._send_cmd([0x45, speed], with_response=False)

    def set_reverse(self, on):
        self._send_cmd([0x46, 0x02 if on else 0x01], with_response=False)

    def __del__(self):
        if self._adapter:
            self._adapter.stop();