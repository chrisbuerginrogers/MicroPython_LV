'''
https://github.com/wipy/wipy/blob/master/docs/User_manual_exp_board.pdf
'''

from machine import Pin
import time
import pycom

pycom.heartbeat(False)

led = Pin('G16',Pin.OUT)
btn = Pin('G17',Pin.IN,Pin.PULL_UP)


led.toggle()
time.sleep(1)
led.value(1)    # 1 is off, 0 is on

btn.value()    # 1 is off, 0 is on

while True:
     led.value(btn.value())
     time.sleep(0.2)