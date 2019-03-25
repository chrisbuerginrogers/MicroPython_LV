'''
https://circuitpython.readthedocs.io/en/2.x/shared-bindings/busio/UART.html
     
connect D3 and D4 to test
'''

import board
from busio import UART

uart=UART(board.D4,board.D3)

uart.write('test')
uart.read(4)

uart.write('test2\n')
uart.readline()  # reads until a \n character
