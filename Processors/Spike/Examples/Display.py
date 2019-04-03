'''
This module controls the 5×5 LED display on the front of the hub. 
It can be used to display images, animations and even text.
'''

import hub,utime

# can display scrolling text or stationary images

hub.display.show(hub.Image.HAPPY)

# You can wait until the previous things is done with  clear=True

# sample callback

def beep():
     hub.sound.volume(10)
     hub.sound.beep(2000, 500, 3)

hub.display.show('LEGO ', loop=False, delay=500, clear = True, fade = 0, callback = beep())

# you can set individual ixels

hub.display.set_pixel(2,3,9)  # x,y, brightness - 0-9

hub.display.get_pixel(2,3)

hub.display.clear()

hub.display.rotation(90)    # can be 0, 90, 180, 270
hub.display.show(hub.Image.HAPPY)
utime.sleep_ms(3000)
hub.display.rotation(0)
hub.display.show(hub.Image.HAPPY)


hub.display.show([hub.Image("09090:99999:99999:09990:00900"),hub.Image("01010:11111:11111:01110:00100")],fade=2,loop=1,delay=500)

hub.display.show(hub.Image.ALL_CLOCKS, loop=True, delay=100)  # note loops forever

hub.display.show('LEGO ', loop=True, delay=500)

hub.display.show('LEGO ', loop=True, fade=4, delay=1000)

hub.display.show(hub.Image.HAPPY, fade=5, delay=2000)

hub.display.show(hub.Image.HAPPY, fade=6, delay=2000)