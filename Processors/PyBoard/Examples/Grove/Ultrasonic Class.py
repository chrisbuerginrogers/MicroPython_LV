'''
http://wiki.seeedstudio.com/Grove-Ultrasonic_Ranger/

connections: 
Ground  - GND 
Power    - 3V3 
NC
Signal - pin Y9
'''

import utime
from machine import Pin,time_pulse_us

class GroveUltrasonic(object):
    def __init__(self, pin):
         self.dio = Pin(pin)

     def value(self):
          dt=-1
          while dt<0:
               self.dio.init(Pin.OUT)
               self.dio.value(0)
               utime.sleep_us(2)
               self.dio.value(1)
               utime.sleep_us(10)
               self.dio.value(0)
               self.dio.init(Pin.IN)
               dt = time_pulse_us(self.dio, 1, 100000)

          return  (dt / 29 / 2)    # cm

sensor = GroveUltrasonic('Y9')
print('Detecting distance...')
while True:
        print('{} cm'.format(sensor.value()))
        utime.sleep(1)