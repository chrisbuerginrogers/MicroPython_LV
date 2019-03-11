'''
http://wiki.seeedstudio.com/Grove-Buzzer/

connections: 
Ground  - GND 
Power    - 3V3 
NC
Signal -  pin Y9
'''

from pyb import Pin

class GroveBuzzer(object):
    def __init__(self, pin):
         self.buzz = Pin(pin,Pin.OUT)

    def value(self):
        return self.buzz.value()

    def toggle(self):
        self.buzz.value(not self.buzz.value())

    def on(self):
         self.buzz.value(True)
        
    def off(self):
         self.buzz.value(False)

import utime
Buzzer = GroveBuzzer('Y9')

Buzzer.off()
utime.sleep(1)
Buzzer.toggle()
utime.sleep(1)
Buzzer.off()

