import machine, radio, utime
from microbit import *

radio.config(channel=7,group=2)
radio.on()

radio.send("hi")
while True:
     radio.receive()


