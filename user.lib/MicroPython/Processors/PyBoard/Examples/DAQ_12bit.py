from pyb import DAC
from array import array
import math

dac = DAC(1, bits=12, buffering=True)   # use 12 bit resolution
dac.write(4095)         # output maximum value, 3.3V


# To output a continuous sine-wave at 12-bit resolution:
# create a buffer containing a sine-wave, using half-word samples
buf = array("H", 2048 + int(2047 * math.sin(2 * math.pi * i / 128)) for i in range(128))

# output the sine-wave at 200Hz
dac.write_timed(buf, 200 * len(buf), mode=DAC.CIRCULAR)