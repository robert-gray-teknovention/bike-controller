from machine import Pin, PWM, Timer
import utime
import time
MID = 1500000
MIN = 1000000
MAX = 2000000



    
led = machine.Pin("LED", machine.Pin.OUT)
relay = machine.Pin(15, machine.Pin.OUT)
while True:
    time.sleep(5)
    relay.high()
    led.low()