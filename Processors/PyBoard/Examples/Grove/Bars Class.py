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
MAX_BRIGHTNESS = 0xFF

class GroveLEDBar(object):
     def __init__(self, dio,clk,RtoG=True):
          self.dio = Pin(dio, Pin.OUT,Pin.PULL_UP)
          self.clk = Pin(clk, Pin.OUT,Pin.PULL_UP)
          self.RtoG = RtoG
          self.stateArray = bytearray(10)
          for i in range(10):
               self.stateArray[i] = 0x00  # allows me to toggle individual elements

     def sendData(self,data):
          state = 0
          for i in range(16):
               state1 = (data & 0x8000)
               self.dio.value(state1)
               state=1-state
               self.clk.value(state)
               data<<=1
          
     def latchData(self):
          self.dio.value(0)
          utime.sleep_ms(10)
          for i in range(4):
               self.dio.value(1)
               utime.sleep_us(1)
               self.dio.value(0)
               utime.sleep_us(1)
          
     def setData(self):
          self.sendData(GLB_CMDMODE)
          for i in range(10):
               self.sendData(self.stateArray[i])
               
          self.sendData(0x00)  
          self.sendData(0x00)
          self.latchData()
          
     def setBits(self,bits):
          for  i in range(10):
               if self.RtoG:
                    j = i
               else:
                    j = 9-i
               if ((bits % 2) == 1):
                    self.stateArray[j] = MAX_BRIGHTNESS
               else:
                    self.stateArray[j] = 0x00
               bits = int(bits / 2)
          self.setData()

     def setBrightness(self,led,brightness):
          led = min(9,max((led-1),0))
          brightness = min (1,max(brightness,0))
          if ~self.RtoG:
               led = 9-led
          self.stateArray[led] =0xFF & ~(~0<< int(8*brightness))
          self.setData()

     def toggleLED(self,led):
          led = min(9,max((led-1),0))
          if ~self.RtoG:
               led = 9-led
          self.stateArray[led] = ~ self.stateArray[led]
          self.setData()
          
     def meter(self,value):
          value = min(10,max(value,0))
          self.setBits(-1 + 2**value)
          

lights = GroveLEDBar('Y9','Y10',False)
lights.setBits(0x3ff)
lights.toggleLED(2)
utime.sleep(1)
lights.toggleLED(2)
lights.setBrightness(3,0.6)

for i in range(11):
     lights.meter(i)
     utime.sleep(.5)



















