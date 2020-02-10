     #!/usr/bin/env pybricks-micropython

'''
grab 10 dots and 10 dashes then test with 5 of each

assumes touch sensor on port 1

'''
from pybricks.hubs import EV3Brick
from pybricks.parameters import Color, Port
from pybricks.ev3devices import (Motor, TouchSensor,
          ColorSensor, UltrasonicSensor, GyroSensor)
from pybricks.tools import wait, StopWatch
import random

# Initialize the EV3
ev3 = EV3Brick()
ev3.speaker.beep()

touch = TouchSensor(Port.S1)
timer = StopWatch()

def Btn():
     while not touch.pressed():
          wait(0.01)
     timer.reset()
     while touch.pressed():
          wait(0.001)
     return timer.time()
     
def train(string, array, num):
     for i in range(num):
          ev3.screen.print('%d: Enter %s' % (num - i,string))
          array[i] =  Btn()

def KNN(cat1, cat2, x, k):
     dist = []
     for data in cat1:
          dist.append((abs(x-data),0))
     for data in cat2:
          dist.append((abs(x-data),1))
     dist.sort()     
     sum = 0
     for i in range(k):
          sum += dist[i][1] 
     return 0 if sum < (k-sum) else 1  # return 0 if mostly 0s
     
def Distance(x,y):
    return ((x - y)*(x - y))

class Kmean():
    def __init__(self,array,k):
        self.array = array
        self.k = k
        self.mean = []
        self.total = []
        self.num = []
        self.lastMean = [0]*k
        
    def findMeans(self):
         for i in range(self.k):
#             x = self.array[random.randint(0,len(self.array)-1)]
             x = random.randint(min(self.array),max(self.array))
             self.mean.append(x)
             self.total.append(x)
             self.num.append(1)
         iteration = 0
         iterate = True
         self.mean.sort()   # make it so 0 == dot

         while(iterate):
             for i in range(self.k):
                 self.lastMean[i] = self.mean[i]
             iteration += 1
             for x in self.array:
                 element = 0
                 minimum = Distance(x,self.mean[element])
                 for i in range(self.k):
                     element = i if (Distance(x,self.mean[i]) < minimum) else element
                 self.num[element] += 1
                 self.total[element] += x
             iterate = False

             for i in range(self.k):
                 self.mean[i] = self.total[i]/self.num[i]
                 iterate = iterate or (abs(self.lastMean[i] - self.mean[i]) > 0.5)
         return self.mean,iteration
        
    def classify(self,x):
        element = 0
        minimum = Distance(x,self.mean[element])
        for i in range(self.k):
            element = i if (Distance(x,self.mean[i]) < minimum) else element
        return element

def readMorse():
     x = Btn()
     guess = (KNN(dots, dashes, x, 3))
     return guess
          
num = 10
testNum = 3
dots = [0]*num
dashes = [0]*num
train('dot', dots, num)
train('dash', dashes, num)
ev3.screen.print('run test')
for i in range(testNum):
          ev3.screen.print('dot' if readMorse() == 0 else 'dash')

times = dots
for i in dashes:
    times.append(i)
km = Kmean(times,2)

means, i = km.findMeans()
print(means)
print('%d iterations - means are %.2f and %.2f' % (i,means[0],means[1]))
for i in range(testNum):
    x = Btn()
    guess = 'dot' if (km.classify(x) == 0) else 'dash'
    ev3.screen.print('%d => %s'%(x,guess))

