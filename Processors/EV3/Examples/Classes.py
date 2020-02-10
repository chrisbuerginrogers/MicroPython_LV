     #!/usr/bin/env pybricks-micropython

'''
grab random numbers and save them to file
'''
from pybricks.hubs import EV3Brick
from pybricks.parameters import Color
from pybricks.tools import wait
import random

def grabNumbers(n):
     a = []
     for i in range(n):
          a.append (random.randint(1,100))
     return a

ev3 = EV3Brick()
ev3.light.on(Color.RED)
array = grabNumbers(10)

for element in array:
     ev3.screen.print(element)
     wait(100)
ev3.light.off()


# or as a class

class Num(object):
     def __init__(self,n):  # this assigns all teh variables belonging to the class instance
          self.size = n
          self.low = 1
          self.high = 100
          self.a = []
          
     def grab(self):
          for i in range(self.size):
               self.a.append (random.randint(self.low,self.high))

fred = Num(10)  
fred.grab()    
for element in fred.a:
     ev3.screen.print(element)

               




