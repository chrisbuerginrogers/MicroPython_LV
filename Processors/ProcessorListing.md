##Processors
#PyBoard
This handy board uses MicroPython.  
A sample code is
'''
import machine

from pyb import Accel


accel = Accel()
print(accel.x(), accel.y(), accel.z(), accel.tilt())
'''