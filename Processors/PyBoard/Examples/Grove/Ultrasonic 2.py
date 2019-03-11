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

dio = Pin('Y9')

def _get_distance():
     dio.init(Pin.OUT)
     dio.value(0)
     utime.sleep_us(2)
     dio.value(1)
     utime.sleep_us(10)
     dio.value(0)
     dio.init(Pin.IN)
     dt = time_pulse_us(dio, 1, _TIMEOUT2)
     if dt<0:
          return None
     distance = (dt / 29 / 2)    # cm
     return distance

def get_distance():
     while True:
          dist = _get_distance()
          if dist:
               return dist

print('Detecting distance...')
while True:
        print('{} cm'.format(get_distance()))
        utime.sleep(1)