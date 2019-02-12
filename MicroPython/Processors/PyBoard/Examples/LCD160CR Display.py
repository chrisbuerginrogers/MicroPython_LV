#from https://github.com/micropython/micropython/blob/master/docs/pyboard/tutorial/lcd160cr_skin.rst


#Try Test
#>>> import lcd160cr_test
#>>> test_all('X')

import lcd160cr
lcd = lcd160cr.LCD160CR('X')
# assumes your display is connected in the X position. If it's in the Y position then use lcd = lcd160cr.LCD160CR('Y') instead.

#To erase the screen and draw a line, try:

lcd.set_pen(lcd.rgb(255, 0, 0), lcd.rgb(64, 64, 128))
lcd.erase()
lcd.line(10, 10, 50, 80)

#draws random rectangles on the screen. You can copy-and-paste it into the MicroPython prompt by first pressing "Ctrl-E" at the prompt, then "Ctrl-D" once you have pasted the text.

from random import randint
for i in range(1000):
    fg = lcd.rgb(randint(128, 255), randint(128, 255), randint(128, 255))
    bg = lcd.rgb(randint(0, 128), randint(0, 128), randint(0, 128))
    lcd.set_pen(fg, bg)
    lcd.rect(randint(0, lcd.w), randint(0, lcd.h), randint(10, 40), randint(10, 40))


#checking touched
lcd.is_touched()  #True?
Touch = lcd.get_touch() #This will return a 3-tuple, with the first entry being 0 or 1 depending on whether there is currently anything touching the screen (1 if there is), and the second and third entries in the tuple being the x and y coordinates of the current (or most recent) touch.


#Connecting the REPL to the display

import pyb
uart = pyb.UART('XA', 115200)
pyb.repl_uart(uart)
