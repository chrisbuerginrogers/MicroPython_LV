from pyb import DAC
import utime,math

dac = DAC(1,buffering=True)            # create DAC 1 on pin X5
dac.write(128)          # write a value to the DAC (makes X5 1.65V)

# To output a continuous sine-wave:

# create a buffer containing a sine-wave
buf = bytearray(100)
for i in range(len(buf)):
    buf[i] = 128 + int(127 * math.sin(2 * math.pi * i / len(buf)))

# output the sine-wave at 400Hz
dac.write_timed(buf, 400 * len(buf), mode=DAC.CIRCULAR)
