#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, 
          ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                   SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import time

# plug in
# A =  left motor
# D =  right motor
# 
# S4 =  ultrasonic sensor

left = Motor(Port.A)
right = Motor(Port.D)
dist = UltrasonicSensor(Port.S4)
wheel_dia = 56
wheel_spacing = 114

car = DriveBase(left,right,wheel_dia,wheel_spacing)
car.drive_time(speed=20,steering= 90,time = 2000)
wait(2000)
car.drive(20,90)
wait(200)
car.stop(Stop.COAST)  #or COAST, BRAKE, or HOLD

brick.sound.beep()
brick.display.clear()
while not any(brick.buttons()):
     measured = dist.distance()
     brick.display.clear()
     brick.display.text(str(measured),(0,60))
     if measured < 2000:
          speed = dist.distance() - 100
          brick.display.text(str(speed))
          car.drive(speed,0)
          wait(10)
