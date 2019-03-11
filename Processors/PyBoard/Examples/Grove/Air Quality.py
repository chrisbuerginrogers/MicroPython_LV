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

while True:
     val = adc.read() / 4096 * 1024
     print ('Quality: %4.2f  or %s' % (val, 'HIGH' if val > 100 else 'LOW'))
     utime.sleep_ms(200)
     
















