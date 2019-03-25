'''
from the main.py file
'''

import board,time
from digitalio import DigitalInOut, Direction, Pull

# Built in red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT
led.value = 1
time.sleep(1)
led.value = 0
