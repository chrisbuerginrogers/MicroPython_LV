'''
http://wiki.seeedstudio.com/Grove-LED_Button/

connections: 
Ground  - GND 
Power    - 3V3 
Signal 2 - button status - pin Y10
Signal1 -  LED status - pin Y9
'''

import pyb,utime

class GroveLEDBtn(object):
    def __init__(self, btn_pin,led_pin):
         self.btn = Pin(btn_pin,Pin.IN)
         self.led = Pin(led_pin,Pin.OUT)

    def value(self):
        return self.btn.value()

    def toggle(self):
        self.led.value(not self.led.value())
        
    def on(self):
         self.led.value(True)
        
    def off(self):
         self.led.value(False)

button = GroveLEDBtn(led_pin = 'Y9',btn_pin = 'Y10')

button.toggle()
button.value()