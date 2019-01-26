# https://github.com/micropython/micropython/blob/master/docs/pyboard/tutorial/timer.rst
import pyb

tim = pyb.Timer(4)
tim.init(freq=10)
tim.callback(lambda t:pyb.LED(1).toggle())
pyb.delay(2000)
tim.callback(None)

     
tim4 = pyb.Timer(4, freq=10)
tim7 = pyb.Timer(7, freq=20)
tim4.callback(lambda t: pyb.LED(1).toggle())
tim7.callback(lambda t: pyb.LED(2).toggle())
pyb.delay(1000)
tim4.callback(None)
tim7.callback(None)
pyb.LED(1).off()
pyb.LED(2).off()