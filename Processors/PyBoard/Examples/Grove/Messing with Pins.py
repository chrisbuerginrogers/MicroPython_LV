'''
https://docs.micropython.org/en/latest/library/pyb.Pin.html

connections: 
Signal -  pin Y9
'''

from pyb import Pin,Timer

Apwm=Pin('Y4',Pin.OUT)
Apwm.af_list()
timer=Timer(3, freq=1000)
chA=timer.channel(4, Timer.PWM, pin=Apwm)
chA.pulse_width_percent(50)
