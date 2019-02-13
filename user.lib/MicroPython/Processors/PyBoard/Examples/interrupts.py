# from https://docs.micropython.org/en/latest/reference/isr_rules.html

import pyb, micropython
micropython.alloc_emergency_exception_buf(100)  # this makes verbose debugging


class LightShow(object):
    def __init__(self,timer, led):
        self.led = led
        timer.callback(self.ToggleIt)
    def ToggleIt (self,line):
        self.led.toggle()

timer1 = pyb.Timer(4, freq=1)
timer2 = pyb.Timer(2, freq=0.8)
led1 =  pyb.LED(1)
led2 = pyb.LED(2)

red = LightShow(timer1,led1)
green = LightShow(timer2,led2 )


# you need to hit Ctrl D to stop the interrupts
