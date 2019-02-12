# from https://learn.sparkfun.com/tutorials/tb6612fng-hookup-guide

# In 1    In2    PWM   Out1    Out2    Mode
#   H       H       H/L       L          L        short break
#   L        H         H        L          H        CCW
#   L        H         L        L          H        short break
#   H        L         H       H          L        CW
#   H        L         L        L          H       short break
#   L         L         L        L          L        Stop

# STBY must be high

from pyb import Pin, Timer

A_PWM = Pin('W29') # W29 has TIM2, CH2
AIn2 = Pin('W22', Pin.OUT)
AIn1 = Pin('W16',Pin.OUT)
Stdby = Pin('W24',Pin.OUT)

BIn1 = Pin('Y12', Pin.OUT)
BIn2 = Pin('W32',Pin.OUT)
B_PWM = Pin('Y11') #  TIM8, CH2

timA = Timer(2, freq=1000)
timB = Timer(8, freq=1000)

SpeedA = -50
SpeedB = 50

Stdby.value(0)  #turn motors off until reset

if (SpeedA < 0):
     AIn1.value(255)
     AIn2.value(0)
     SpeedA = - SpeedA
else:
     AIn1.value(0)
     AIn2.value(255)

if (SpeedB < 0):
     BIn1.value(255)
     BIn2.value(0)
     SpeedB = - SpeedB
else:
     BIn1.value(0)
     BIn2.value(255)

chA = timA.channel(2, Timer.PWM, pin= A_PWM)
chA.pulse_width_percent(SpeedA)
chB = timB.channel(2, Timer.PWM, pin= B_PWM)
chB.pulse_width_percent(SpeedB)

Stdby.value(255)  #everything is ready - reset motors
