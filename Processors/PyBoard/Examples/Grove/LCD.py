'''
http://wiki.seeedstudio.com/Grove-LCD_RGB_Backlight/

connections: 
Ground (B) - GND 
Power  (R)   - Needs to be 5 volts for the text to work 
SCLK - pin Y9
SDATA -  pin Y10
'''

from machine import I2C
import utime

i2c = I2C(2)  
i2c.scan()

TEXT_ADDR = 0x3E   #62
RGB_ADDR = 0x62    #98

def setRGB(r,g,b):
     i2c.writeto_mem(RGB_ADDR, 0x00,b'\x00')
     i2c.writeto_mem(RGB_ADDR, 0x01,b'\x00')
     i2c.writeto_mem(RGB_ADDR, 0x08,b'\xAA')
     i2c.writeto_mem(RGB_ADDR, 0x04, chr(r))
     i2c.writeto_mem(RGB_ADDR, 0x03,  chr(g))
     i2c.writeto_mem(RGB_ADDR, 0x02,  chr(b))

def textCommand(cmd):
     i2c.writeto_mem(TEXT_ADDR, 0x80, chr(cmd)) #byte out, slave addr, starting memory location on slave

def setText(text):
     textCommand(0x02)   # 1 = clear display 2 = reset cursor to home
     utime.sleep_ms(50)
     textCommand(0x08 | 0x04) # display on, no cursor
     textCommand(0x28) # 2 lines
     utime.sleep_ms(50)
     count = 0
     row = 0
     while len(text) < 32: # clears the rest of the screen
          text += " " 
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
          i2c.writeto_mem(TEXT_ADDR, 0x40,c)

setRGB(0,255,0)
setText("Hi \nKim")














