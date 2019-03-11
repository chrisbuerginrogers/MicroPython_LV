import machine

from pyb import Accel


accel = Accel()
print(accel.x(), accel.y(), accel.z(), accel.tilt())
