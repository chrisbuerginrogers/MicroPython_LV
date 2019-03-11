'''
http://wiki.seeedstudio.com/Grove-Ultrasonic_Ranger/

connections: 
Ground  - GND 
Power    - 3V3 
NC
Signal - pin Y9
'''

import utime
from machine import Pin


dio = Pin('Y9')

def _get_distance():
     dio.init(Pin.OUT)
     dio.value(0)
     utime.sleep_us(2)
     dio.value(1)
     utime.sleep_us(10)
     dio.value(0)

     dio.init(Pin.IN)

     t0 = utime.ticks_us()
     count = 0
     while count < _TIMEOUT1:
          if dio.value():
               break
          count += 1
          if count >= _TIMEOUT1:
               return None
     t1 = utime.ticks_us()
     count = 0
     while count < _TIMEOUT2:
          if not dio.value():
               break
          count += 1
          if count >= _TIMEOUT2:
               return None
     t2 = utime.ticks_us()
     dt = int(t1 - t0)
     if dt > 530:
          return None
     distance = ((t2 - t1) / 29 / 2)    # cm
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
