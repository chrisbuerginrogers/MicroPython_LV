'''
Motion is an object that controls the movement sensors.
'''

import hub,utime

hub.motion.accelerometer()

hub.motion.gyroscope()

hub.motion.position()

hub.motion.orientation()  # has a callback option

def beep():
     hub.sound.volume(10)
     hub.sound.beep(2000, 500, 3)

hub.motion.callback(beep())

hub.motion.gesture('down')  # is it currently active?

hub.motion.was_gesture('down')  # has it been active since the last call?



'''
possible gestures:

leftside
rightside
down
up
front
back
tapped
doubletapped
shake
freefall
'''