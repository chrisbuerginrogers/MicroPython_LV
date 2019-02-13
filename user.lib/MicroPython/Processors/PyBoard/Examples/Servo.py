#  from https://github.com/micropython/micropython/blob/master/docs/pyboard/tutorial/servo.rst

import pyb

servo1 = pyb.Servo(1)   # pix X1

#set the angle
servo1.angle(45)

#read the angle
servo1.angle()

# move two servos at the same time with speed control
servo2 = pyb.Servo(2)   
servo1.angle(-45, 2000); servo2.angle(60, 2000)

# continuous rotation
servo1.speed()

# you can also change the calibration (see webpage)
