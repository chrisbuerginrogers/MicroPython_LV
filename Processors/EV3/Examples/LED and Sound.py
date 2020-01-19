#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import Button, Color,ImageFile
from pybricks.tools import print, wait

# A high pitch (1500 Hz) for one second (1000 ms) at 50% volume
brick.sound.beep(500, 1000, 20)

while True:
    # Do something if the left button is pressed
    if Button.LEFT in brick.buttons():
        print("The left button is pressed.")
        break
    wait(100)
brick.light(Color.RED)
Light = [Color.BLACK, Color.GREEN, Color.YELLOW, Color.RED, Color.ORANGE]

for color in Light:
    print(color)
    try:
        brick.light(color)
    except:
        print('bad')
    wait(500)

brick.display.clear()
brick.display.text(brick.battery.voltage(), (0, 50))
while not Button.CENTER in brick.buttons():
    wait(100)
brick.display.image(ImageFile.UP)
while not Button.CENTER in brick.buttons():
    wait(100)
