'''
http://wiki.seeedstudio.com/Grove-Relay/

connections: 
Ground  - GND 
Power    - 3V3 
NC
Signal -  pin Y9
'''

import pyb,utime

Relay = pyb.Pin('Y9', pyb.Pin.OUT)

Relay.on()
utime.sleep_ms(200)
Relay.off()

