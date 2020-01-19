#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, 
          ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                   SoundFile, ImageFile, Align)
from pybricks.tools import print, wait

# plug in
# S1 =  touch sensor 
# S2 =  light sensor
# S3 =  gyro sensor
# S4 =  ultrasonic sensor

touch = TouchSensor(Port.S1)
while not touch.pressed():
     wait (10)
     
light = ColorSensor(Port.S2)
light.rgb()
wait(100)
light.color()  
# returns Color.BLACK, Color.BLUE, Color.GREEN, Color.YELLOW, Color.RED, Color.WHITE, Color.BROWN or None.
wait(100)
while not (light.color() == Color.YELLOW):
     wait(100)
light.reflection()
wait(100)
light.ambient()
wait(100)

gyro = GyroSensor(Port.S3)

gyro.reset_angle(0)  # define your starting angle
while gyro.angle() < 90:
     wait(100)
     
gyro.speed()