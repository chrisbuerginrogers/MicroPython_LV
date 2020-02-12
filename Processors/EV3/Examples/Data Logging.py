#!/usr/bin/env pybricks-micropython
#brickrun -r -- pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.parameters import Color, Port
from pybricks.ev3devices import Motor
from pybricks.iodevices import AnalogSensor, UARTDevice

# Initialize the EV3
ev3 = EV3Brick()
ev3.speaker.beep()
sense = AnalogSensor(Port.S1, False)
sense.voltage()

watch = StopWatch()
wheel = Motor(Port.A)
data = DataLog('output.txt', header = 'Time,Angle,Voltage')

# Turn on a red light
ev3.light.on(Color.RED)
ev3.speaker.say("About to take data")
wheel.run(500)

for i in range(10):
    time = watch.time()
    angle = wheel.angle()
    light = sense.voltage()   #This seems to give a EIO error sometimes.
    data.log(time,angle,light)
    wait(100)

# Turn the light off
ev3.light.off()