     #!/usr/bin/env pybricks-micropython

'''
see different ways of using callbacks
'''
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, 
          ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                   SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import time

# Initialize the EV3
ev3 = EV3Brick()
ev3.speaker.beep()

# Timer Callback

def timerCallback(timerInfo):
     ev3.screen.print('time')
     
txTimer = 4
sendTimer = pyb.Timer(txTimer, freq = freq)  # default is 200 ms
sendTimer.callback(timerCallback)
sendTimer.callback(None)  # close callback
