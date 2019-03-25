'''
https://www.amazon.com/ELEGOO-28BYJ-48-ULN2003-Stepper-Arduino/dp/B01CP18J4A?ref_=fsclp_pl_dp_2     

connections: 
Ground (B) - GND 
Power  (R)   - separate 5v power supply 
IN1 = W29
IN2 = W24
IN3 = W22
IN4 = W16
'''

from pyb import Pin
import utime

sequence = [(0,0,0,1),(0,0,1,1),(0,0,1,0),(0,1,1,0),
                    (0,1,0,0),(1,1,0,0),(1,0,0,0),(1,0,0,1)]


IN1 = Pin('W29',Pin.OUT)
IN2 = Pin('W24',Pin.OUT)
IN3 = Pin('W22',Pin.OUT)
IN4 = Pin('W16',Pin.OUT)

def stepper(Steps,Direction):
     steps = 0
     for i in range(Steps):
#          print(str(steps) + ' : ' + str(sequence[steps]))
          utime.sleep_us(800)
          IN1.value(sequence[steps][0])
          IN2.value(sequence[steps][1])
          IN3.value(sequence[steps][2])
          IN4.value(sequence[steps][3])
          if Direction:
               steps += 1
          else:
               steps -= 1
          if steps < 0:
               steps = 7
          elif steps > 7:
               steps = 0
     return Steps


for i in range(10):
     rotations = 1.5
     steps = int(rotations * 4096)
     stepper(steps,True)
     utime.sleep(1)

















