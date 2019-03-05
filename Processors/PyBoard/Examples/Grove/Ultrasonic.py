import utime
from machine import Pin

_TIMEOUT1 = 1000
_TIMEOUT2 = 10000

class GroveUltrasonicRanger(object):
    def __init__(self, pin):
        self.dio = Pin(pin,Pin.OUT,Pin.PULL_UP)

    def _get_distance(self):
        self.dio.init(Pin.OUT)
        self.dio.value(0)
        utime.sleep_us(2)
        self.dio.value(1)
        utime.sleep_us(10)
        self.dio.value(0)

        self.dio.init(Pin.IN,Pin.PULL_UP)

        t0 = utime.time()
        count = 0
        while count < _TIMEOUT1:
            if self.dio.value():
                break
            count += 1
        if count >= _TIMEOUT1:
            return None

        t1 = utime.time()
        count = 0
        while count < _TIMEOUT2:
            if not self.dio.value():
                break
            count += 1
        if count >= _TIMEOUT2:
            return None

        t2 = utime.time()

        dt = int((t1 - t0) * 1000000)
        if dt > 530:
            return None

        distance = ((t2 - t1) * 1000000 / 29 / 2)    # cm

        return distance

    def get_distance(self):
        while True:
            dist = self._get_distance()
            if dist:
                return dist

sonar = GroveUltrasonicRanger('Y9')

print('Detecting distance...')
while True:
        print('{} cm'.format(sonar.get_distance()))
        utime.sleep(1)

