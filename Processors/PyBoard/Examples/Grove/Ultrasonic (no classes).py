import utime
from machine import Pin

_TIMEOUT1 = 1000
_TIMEOUT2 = 10000
_TIMEOUT = 100000

dio = Pin('Y9',Pin.OUT,Pin.PULL_UP)

def _get_distance():
     dio.init(Pin.OUT)
     dio.value(0)
     utime.sleep_us(2)
     dio.value(1)
     utime.sleep_us(10)
     dio.value(0)

     dio.init(Pin.IN,Pin.PULL_UP)

     t0 = utime.ticks_us()
     count = 0
     while count < _TIMEOUT:
          if dio.value():
               break
          count += 1
          if count >= _TIMEOUT:
               return None

     t1 = utime.ticks_us()
     count = 0
     while count < _TIMEOUT:
          if not dio.value():
               break
          count += 1
          if count >= _TIMEOUT:
               return None

     t2 = utime.ticks_us()
#     dt = int(t1 - t0)
#     if dt > 530:
#          return None
     distance = ((t2 - t1) / 29 / 2)    # cm
     return distance

def get_distance():
     while True:
          dist = _get_distance()
          if dist:
               return dist

print('Detecting distance...')
while True:
        print('{} cm'.format(sonar.get_distance()))
        utime.sleep(1)

