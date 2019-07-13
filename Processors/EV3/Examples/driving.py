#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import time

# Write your program here
left = Motor(Port.A)
right = Motor(Port.D)
wheel_dia = 56
wheel_spacing = 114

car = DriveBase(left,right,wheel_dia,wheel_spacing)
brick.sound.beep()
brick.display.clear()
while not any(brick.buttons()):
    speed = UltrasonicSensor(Port.S4) - 10
    brick.display.text(str(speed),(0,60))
    car.drive(speed)
    wait(10)
