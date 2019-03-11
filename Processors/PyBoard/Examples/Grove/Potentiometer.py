'''
http://wiki.seeedstudio.com/Grove-Rotary_Angle_Sensor/

connections: 
Ground  - GND 
Power    - 3V3 
NC
Signal -  pin W24
'''

import pyb,utime

adc = pyb.ADC('W24')

while True:
     val = adc.read()
     print ('%4.2f' % val)
     utime.sleep_ms(200)
     