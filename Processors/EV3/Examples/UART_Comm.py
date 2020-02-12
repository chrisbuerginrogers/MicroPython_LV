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

uart = UARTDevice(Port.S1, 9600, timeout=2000)
# short pins 5/6 (blue and yellow)
uart.write('Test')
wait(10)
data = uart.read_all()  #if you connect Pin 5 & 6 you should see Test on the screen
ev3.screen.print(data)

uart.write('Test')
uart.waiting() # how many bytes on the port
uart.read(uart.waiting())

# Turn the light off
ev3.light.off()