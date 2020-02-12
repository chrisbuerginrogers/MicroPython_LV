#!/usr/bin/env pybricks-micropython

'''
This reads the USB serial line on the EV3 as fast as possible
and assumes that data is coming from the Arduino much faster
than we can read it - so it grabs all the data, splits it up into an array,
and then takes the second to last element of that array to get an
array of accelerations and angular accelerations.

The 6 elements are:
     x acceleration
     y acceleration
     z acceleration
     x gyro
     y gyro
     z gyro
     
Note that I take the second to last line because the last line might be incomplete
(who knows where in the serial transmission the line is when I do the read).
''''

import serial
s=serial.Serial("/dev/ttyACM0",9600)
for i in range(10):
     data=s.read(s.inWaiting()).decode("utf-8")
     #print('size = %d, buffer = %d' % (len(data),s.inWaiting()))
     data = data.splitlines()
     imu = data[-2].split(',')
     #print(imu)
     