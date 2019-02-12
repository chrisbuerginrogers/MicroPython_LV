# Old |      New Value
#        |    0    1   2   3
#   0   |    0   -1  1   X
#   1   |    1    0   X  -1
#   2   |   -1   X   0   1
#   3   |    X    1  -1  0


# From https://cdn.sparkfun.com/datasheets/Robotics/How%20to%20use%20a%20quadrature%20encoder.pdf

from pyb import Pin
import array
import utime

M1_New = 0
M1_EncA = Pin('Y1', Pin.IN, pull = Pin.PULL_UP)
M1_EncB = Pin('Y2', Pin.IN, pull = Pin.PULL_UP)

M1_Matrix = array.array('l',[0,-1,1,2,1,0,2,-1,-1,2,0,1,2,1,-1,0])

#To read the array my index is: Old * 4 + New So my code reads like this:
while True:
     M1_Old = M1_New
     M1_New = M1_EncA.value()  * 2 + M1_EncB.value()
     Out = M1_Matrix [M1_Old * 4 + M1_New]
     print('Old: %2d   New: %2d    Out %2d' % (M1_Old, M1_New, Out))
     utime.sleep(0.01)
