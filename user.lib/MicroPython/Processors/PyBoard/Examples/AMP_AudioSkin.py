# from https://github.com/micropython/micropython/blob/master/docs/pyboard/tutorial/amp_skin.rst

import pyb

def volume(val):
    pyb.I2C(1, pyb.I2C.MASTER).mem_write(val, 46, 0)

#>>> volume(0)   # minimum volume
#>>> volume(127) # maximum volume

#To play a sound, use the write_timed method of the DAC object. For example:

import math
from pyb import DAC

# create a buffer containing a sine-wave
buf = bytearray(100)
for i in range(len(buf)):
    buf[i] = 128 + int(127 * math.sin(2 * math.pi * i / len(buf)))

# output the sine-wave at 400Hz
dac = DAC(1)
dac.write_timed(buf, 400 * len(buf), mode=DAC.CIRCULAR)

# or playing a wave file from the SD Card

import wave
from pyb import DAC
from pyb import delay
dac = DAC(1)

def play(filename):
    f = wave.open(filename, 'r')
    total_frames = f.getnframes()
    framerate = f.getframerate()

    for position in range(0, total_frames, framerate):
        f.setpos(position)
        dac.write_timed(f.readframes(framerate), framerate)
        delay(1000)
