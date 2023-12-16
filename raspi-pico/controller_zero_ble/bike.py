
def at_speed():
    relay.high()
    
    battery_charge_delay_timer.init(period=30000, mode=Timer.ONE_SHOT, callback= lambda t:charge_timer_elapsed())
    print("at speed")

def charge_timer_elapsed():
    print ("Charge Timer elapsed")
    relay.low()

def run_bike():
    import machine
    import utime
    import time
    from machine import Timer
    MID = 1500000
    MIN = 1000000
    MAX = 2000000
      
    led = machine.Pin("LED", machine.Pin.OUT)
    relay = machine.Pin(15, machine.Pin.OUT)
    
    relay.low()
    ir_sensor = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
    print ("We are starting the bike!")
    last_state = 0
    counter = 0
    delta = 0
    start = time.ticks_ms()
    rpm = 0
    on_rpm = 100
    at_rpm_timer = Timer(-1)
    battery_charge_delay_timer = Timer(-1)
    at_rpm_timer_status=False
    relay_second_count = 5
    count = 0
    while True:
        
        light = ir_sensor.value()
        if light:
            #led.high()
            
            if last_state:
                last_state = False
                
                
        else:
            # led.high()
            
            if not last_state:
                last_state = True
                counter+=1
                delta = time.ticks_diff(time.ticks_ms(),start)
                start=time.ticks_ms()
                #print ("Revolutions: ",counter)
                #print ("Time in ms: ", delta)
                
                if delta > 0:
                    rpm = 1/delta*60 * 1000
                    #print ("rpm: ", rpm)
    
        #if rpm > on_rpm:
        if True:
            led.high()
            if count < relay_second_count:
                relay.high()
                time.sleep(1)
                count += 1
            else:
                relay.low()
                # at_rpm_timer_status = True
                
            '''if not at_rpm_timer_status:
                at_rpm_timer.init(period=30000, mode=Timer.ONE_SHOT, callback= lambda t:at_speed())
                at_rpm_timer_status = True
                pass'''
            
                
        else:
            led.low()
            relay.low()
            # at_rpm_timer_status = False
            '''if at_rpm_timer_status:
                at_rpm_timer.deinit()
                battery_charge_delay_timer.deinit()
            at_rpm_timer_status = False'''
            
            
            pass
            
        
    