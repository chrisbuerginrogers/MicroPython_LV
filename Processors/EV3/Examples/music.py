#!/usr/bin/env pybricks-micropython

'''
This plays a scale
''''

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.parameters import Port
from pybricks.ev3devices import UltrasonicSensor


# Initialize the EV3
ev3 = EV3Brick()
ev3.speaker.beep(440,500)
ev3.speaker.beep(880,500)
ev3.speaker.beep(440,500)
ev3.speaker.beep(220,500)
ev3.speaker.beep(440,500)

# or if you want to do soem thinking while the notes are playing
ev3.speaker.beep(440,-1)
wait (100) # note we wait a little and then change the note frequency
ev3.speaker.beep(880,500)

# or for the more musically inclined
notes = ['G3/8','G3/8', 'G3/8', 'Eb3/2','R/8','F3/8','F3/8', 'F3/8', 'D3/2']
ev3.speaker.play_notes(notes, tempo=120)

# or if you want to make a theremin
dist = UltrasonicSensor(Port.S4)
while True:
     tone = dist.distance()*5
     ev3.speaker.beep(tone,-1)
     wait(10)

