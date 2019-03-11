'''
http://wiki.seeedstudio.com/Grove-Temperature_Sensor_V1.2/

connections: 
Ground (B) - GND 
Power  (R)   - 3V3 
NC
Signal -  pin W24
'''

from pyb import ADC
import math

B = 4275             # B value of the thermistor
R0 = 100000      #R0 = 100k

class GroveTemp(object):
     def __init__(self, pin):
          self.adc = ADC(pin)

     def value(self):
          val = adc.read()
          R = 4095/val-1.0
          R = R0*R
          temperature = 1.0/(math.log10(R/R0)/B+1/298.15)-273.15 
          return temperature
          
import utime

temp = GroveTemp('W24')
while True:
     print ('%4.2f' % (temp.value()))
     utime.sleep_ms(200)
     


