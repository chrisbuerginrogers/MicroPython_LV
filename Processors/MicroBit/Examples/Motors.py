import machine, utime
from microbit import *


for fred in range(5):
     pin1.write_digital(0)
     pin15.write_analog(512)
     pin8.write_digital(0)
     pin16.write_analog(512)
     
     utime.sleep_ms(500)


