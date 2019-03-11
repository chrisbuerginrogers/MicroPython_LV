'''
http://wiki.seeedstudio.com/Grove-Sound_Sensor/

connections: 
Ground (B) - GND 
Power  (R)   - 3V3 
NC
Signal -  pin W24
'''

import pyb,utime

adc = pyb.ADC('W24')

size = 100
while True:
     val = 0
     for i in range (size):
          val = val + adc.read()
     val = val / size
     print ('Sound: %4.2f' % val)
     utime.sleep_ms(200)
     











