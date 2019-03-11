'''
http://wiki.seeedstudio.com/Grove-Button/

connections: 
Ground  - GND 
Power    - 3V3 
NC
Signal -  pin Y9
'''

from pyb import Pin

class GroveButton(object):
    def __init__(self, pin):
         self.button = Pin(pin,Pin.IN)

    def value(self):
        return self.button.value()
        
button = GroveButton('Y9')
button.value()