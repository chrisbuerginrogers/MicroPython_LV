'''
http://wiki.seeedstudio.com/Grove-Sound_Sensor/

connections: 
Ground (B) - GND 
Power  (R)   - 3V3 
NC
Signal -  pin W24
'''

from pyb import ADC

class GroveSPL(object):
     def __init__(self, pin):
          self.adc = ADC(pin)

     def value(self):
          val = 0
          for i in range (100):
               val = val + self.adc.read()
          val = val / 100
          return val
          
import utime

sound = GroveSPL('W24')
while True:
     print ('%4.2f' % (sound.value()))
     utime.sleep_ms(200)
     




