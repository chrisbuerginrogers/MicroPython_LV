'''
http://wiki.seeedstudio.com/Grove-Sound_Sensor/

connections: 
Ground (B) - GND 
Power  (R)   - 3V3 
NC
Signal -  pin W24
'''

from pyb import ADC

class GroveAirQuality(object):

     def __init__(self, pin):
          self.adc = ADC(pin)

     @property
     def value(self):
          return self.adc.read() / 4096 * 1024

import utime

air = GroveAirQuality('W24')
while True:
     print ('Quality: %4.2f  or %s' % (val, 'HIGH' if val > 100 else 'LOW'))
     utime.sleep_ms(200)
     





