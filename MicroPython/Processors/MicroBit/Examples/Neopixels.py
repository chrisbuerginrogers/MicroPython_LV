import machine, neopixel, utime
from microbit import *

np = neopixel.NeoPixel(pin2, 10)
from microbit import *


np.clear()
for fred in range(len(np)):
     np[fred] = (220,0,40)
     np.show()
     utime.sleep_ms(500)


np.clear()
