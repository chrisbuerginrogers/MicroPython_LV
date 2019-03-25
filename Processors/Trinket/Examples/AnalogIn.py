'''
from the main.py file
'''

import board
from analogio import AnalogIn

# Helper to convert analog input to voltage
def getVoltage(pin):
    return (pin.value * 3.3) / 65536

# Analog input on D0
analog1in = AnalogIn(board.D0)

# Read analog voltage on D0
print("D0: %0.2f" % getVoltage(analog1in))

