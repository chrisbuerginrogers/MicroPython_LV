'''
http://wiki.seeedstudio.com/Grove-Button/

connections: 
Ground  - GND 
Power    - 3V3 
NC
Signal -  pin Y9
'''

import pyb,utime

button = pyb.Pin('Y9',pyb.Pin.IN)

button()
utime.sleep(2)
button()
