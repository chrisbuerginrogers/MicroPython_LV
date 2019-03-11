'''
http://wiki.seeedstudio.com/Grove-Rotary_Angle_Sensor/

connections: 
Ground  - GND 
Power    - 3V3 
NC
Signal -  pin W24
'''

from pyb import ADC

class GroveAngle(object):
    def __init__(self, pin):
         self.adc = ADC(pin)

    def value(self):
        return self.adc.read()
        
import utime

val = GroveAngle('W24')
while True:
     print ('%4.2f' % (val.value()/4095.0*360.0))
     utime.sleep_ms(200)
     