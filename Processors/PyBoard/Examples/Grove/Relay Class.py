'''
http://wiki.seeedstudio.com/Grove-Relay/

connections: 
Ground  - GND 
Power    - 3V3 
NC
Signal -  pin Y9
'''

from pyb import Pin

class GroveRelay(object):
    def __init__(self, pin):
         self.relay = Pin(pin,Pin.OUT)

    def value(self):
        return self.relay.value()

    def toggle(self):
        self.relay.value(not self.relay.value())

    def on(self):
         self.relay.value(True)
        
    def off(self):
         self.relay.value(False)

import utime
Relay = GroveRelay('Y9')

Relay.on()
utime.sleep_ms(200)
Relay.off()
utime.sleep_ms(200)
Relay.toggle()
Relay.value()
