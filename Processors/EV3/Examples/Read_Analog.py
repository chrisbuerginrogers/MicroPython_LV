#!/usr/bin/env pybricks-micropython

'''
This code will set up port 1 as an analog in port
Make sure to use pin 6 as AIN rather than Pin 1 (otherwise you will need to get the right resistors on Pin2)

'''

from pybricks.parameters import Port
from pybricks.ev3devio import Ev3devSensor

class EV3Sensor(Ev3devSensor):
    _ev3dev_driver_name='ev3-analog-01'
    def read(self):
        self._mode('ANALOG')
        return self._value(0)

# this is a hack to set the mode properly
from ev3dev2.port import LegoPort
s = LegoPort(address ='ev3-ports:in1')
s.mode = 'ev3-analog'

# now set up your sensor to read
sensor=EV3Sensor(Port.S1) # same port as above
print(sensor.read())