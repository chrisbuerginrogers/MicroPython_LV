import machine, utime
from microbit import *


for fred in range(5):
     display.scroll(fred)
     utime.sleep_ms(500)


