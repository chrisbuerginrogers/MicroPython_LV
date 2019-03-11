'''
http://wiki.seeedstudio.com/Grove-LED_Button/

connections: 
Ground  - GND 
Power    - 3V3 
Signal 2 - button status - pin Y10
Signal1 -  LED status - pin Y9
'''

import pyb,utime

Btn = pyb.Pin('Y10', pyb.Pin.IN)
LED = pyb.Pin('Y9', pyb.Pin.OUT)

Btn.value()

def btn_callback(line):
        if LED.value():
             LED.off()
        else:
             LED.on()

Btn_interrupt = pyb.ExtInt(Btn, pyb.ExtInt.IRQ_FALLING, pyb.Pin.PULL_NONE, btn_callback)
