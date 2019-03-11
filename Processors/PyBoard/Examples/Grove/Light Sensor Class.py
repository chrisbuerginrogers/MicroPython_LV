'''
http://wiki.seeedstudio.com/Grove-Light_Sensor/

connections: 
Ground  - GND 
Power    - 3V3 
NC
Signal - A0
'''

from pyb import ADC

class GroveLight(object):
    def __init__(self, pin):
         self.adc = ADC(pin)

    def value(self):
        return self.adc.read()
        
import utime

Light = GroveLight('W24')
while True:
     Light.value()
     utime.sleep_ms(200)