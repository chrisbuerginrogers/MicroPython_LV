'''
from the main.py file
'''


import board
from analogio import AnalogOut
import time

# Analog output on D1
aout = AnalogOut(board.D1)

i=0
while True:
    # set analog output to 0-3.3V (0-65535 in increments)
    aout.value = i * 256
    i = (i+1) % 256  # run from 0 to 255
