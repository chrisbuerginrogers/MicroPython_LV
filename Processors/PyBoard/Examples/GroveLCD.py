from pyb import I2C
import utime

i2c = I2C(1, I2C.MASTER)  


TEXT_ADDR = 0x3e
RGB_ADDR = 0x62

def setRGB(r,g,b):
    i2c.mem_write(0x00, RGB_ADDR, 0x00)
    i2c.mem_write(0x00, RGB_ADDR, 0x01)
    i2c.mem_write(0xAA, RGB_ADDR, 0x08)
    i2c.mem_write(r, RGB_ADDR, 0x04)
    i2c.mem_write(g, RGB_ADDR, 0x03)
    i2c.mem_write(b, RGB_ADDR, 0x02)

def textCommand(cmd):
    i2c.mem_write(cmd, TEXT_ADDR, 0x80) #byte out, slave addr, starting memory location on slave

def setText(text):
    textCommand(0x02)   # 1 = clear display 2 = reset cursor to home
    utime.sleep_ms(50)
    textCommand(0x08 | 0x04) # display on, no cursor
    textCommand(0x28) # 2 lines
    utime.sleep_ms(50)
    count = 0
    row = 0
#  makes it so you do not need to reset the screen
    while len(text) < 32: # clears the rest of the screen
        text += " " 
#
    for c in text:
        if c == "\n" or count == 16:
            count = 0
            row += 1
            if row == 2:
                break
            textCommand(0xC0)
            if c == "\n":
                continue
        count += 1
        i2c.mem_write(ord(c), TEXT_ADDR, 0x40)

setRGB(0,255,0)
setText("Hi \nKim")