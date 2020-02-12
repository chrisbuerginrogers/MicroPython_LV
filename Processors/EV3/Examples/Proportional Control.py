     #!/usr/bin/env pybricks-micropython

'''
This code determines the minimum sampling time:
     DriveBase - 5 ms
     single motor = 0.6 ms
'''

from pybricks.hubs import EV3Brick
from pybricks.tools import wait,StopWatch,DataLog
from pybricks.parameters import Color, Port
from pybricks.ev3devices import (Motor, 
          ColorSensor, UltrasonicSensor, GyroSensor)
from pybricks.robotics import DriveBase

# Initialize the EV3
ev3 = EV3Brick()
ev3.light.on(Color.RED)
left = Motor(Port.A)
right = Motor(Port.D)
dist = UltrasonicSensor(Port.S4)
wheel_dia = 56
wheel_spacing = 114

car = DriveBase(left,right,wheel_dia,wheel_spacing)
timer = StopWatch()
data = DataLog('output.txt', header = 'iteration,Base time, motor time')

Iteration = 1000
def testBase():
     timer.reset()
     for i in range(Iteration):
          speed = dist.distance()
          car.drive(speed,0)
     duration = timer.time()
     car.stop()
     return duration
     
def testMotor():
     timer.reset()
     for i in range(Iteration):
          speed = dist.distance()
          left.run(speed)
     duration = timer.time()
     left.stop()
     return duration

for i in range(10):
     base = testBase()
     motor = testMotor()
     print('%d  %d' % (base,motor))
     data.log(i,base,motor)

ev3.light.off()







