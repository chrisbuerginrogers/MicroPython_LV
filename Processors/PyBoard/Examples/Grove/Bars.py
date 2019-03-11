'''
http://wiki.seeedstudio.com/Grove-LED_Bar/
https://github.com/Seeed-Studio/Grove_LED_Bar/blob/master/Grove_LED_Bar.cpp
https://github.com/Seeed-Studio/Grove_LED_Bar/blob/master/examples/BasicControl/BasicControl.ino

connections: 
Ground (B) - GND 
Power  (R)   - 3V3 
DCLK (W) - pin Y9
DIn (Y) -  pin Y10
'''

import  utime
from machine import Pin

GLB_CMDMODE = 0x00  # Work on 8-bit mode

dio = Pin('Y9', Pin.OUT,Pin.PULL_UP)
clk = Pin('Y10', Pin.OUT,Pin.PULL_UP)

def sendData(data):
     state = 0
     for i in range(16):
          state1 = (data & 0x8000)

          dio.value(state1)
          state=1-state
          clk.value(state)
          data<<=1
          
def latchData():
     dio.value(0)
     utime.sleep_ms(10)
     for i in range(4):
          dio.value(1)
          utime.sleep_us(1)
          dio.value(0)
          utime.sleep_us(1)
          
def setData(state):
     sendData(GLB_CMDMODE)
     for i in range(10):
          sendData(state[i])
          
# Two extra empty bits for padding the command to the correct length
     sendData(0x00)
     sendData(0x00)
     latchData()
          
def setBits(bits):
     state = bytearray(10)
     for  i in range(10):
           if ((bits % 2) == 1):
                state[i] = 0xFF
           else:
                state[i] = 0x00
           bits = int(bits / 2)
     setData(state)
        
setBits(0x3ff)
