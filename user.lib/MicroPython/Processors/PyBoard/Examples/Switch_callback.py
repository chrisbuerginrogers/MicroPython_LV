# from http://docs.micropython.org/en/v1.8.4/pyboard/pyboard/tutorial/switch.html

import pyb

sw = pyb.Switch()

# find the current state of hte switch
sw()

#set up a callback
sw.callback(lambda:pyb.LED(1).toggle())
     
# disable callback
sw.callback(None)

# or use a defined function instead of lambda
def f():
     pyb.LED(1).toggle()

sw.callback(f)