'''
http://wiki.seeedstudio.com/Grove-Light_Sensor/

connections: 
Ground  - GND 
Power    - 3V3 
NC
Signal - A0
'''

import pyb,utime

Light = pyb.ADC('W24')

while True:
     Light.read()
     utime.sleep_ms(200)