'''
http://wiki.seeedstudio.com/Grove-Buzzer/

connections: 
Ground  - GND 
Power    - 3V3 
NC
Signal -  pin Y9
'''

import pyb,utime

Buzzer = pyb.Pin('Y9', pyb.Pin.OUT)

Buzzer.value(1)
utime.sleep(1)
Buzzer.value(0)

