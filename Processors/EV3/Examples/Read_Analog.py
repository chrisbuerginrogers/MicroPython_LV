#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.parameters import Color, Port
from pybricks.iodevices import AnalogSensor

# Initialize the EV3
ev3 = EV3Brick()
ev3.light.on(Color.RED)
sense = AnalogSensor(Port.S1, False)
sense.voltage()

for i in range(100):
    light = sense.voltage()   #This seems to give a EIO error sometimes.
    ev3.screen.print(light)
    wait(100)

ev3.light.off()