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

TEXT_ADDR = 0x3E   #62
RGB_ADDR = 0x62    #98

class GroveRGB_LCD(object):
     def __init__(self, i2c):
          self.i2c = I2C(i2c)

     def setRGB(self,r,g,b):
          self.i2c.writeto_mem(RGB_ADDR, 0x00,b'\x00')
          self.i2c.writeto_mem(RGB_ADDR, 0x01,b'\x00')
          self.i2c.writeto_mem(RGB_ADDR, 0x08,b'\xAA')
          self.i2c.writeto_mem(RGB_ADDR, 0x04, chr(r))
          self.i2c.writeto_mem(RGB_ADDR, 0x03,  chr(g))
          self.i2c.writeto_mem(RGB_ADDR, 0x02,  chr(b))

     def textCommand(self,cmd):
          self.i2c.writeto_mem(TEXT_ADDR, 0x80, chr(cmd)) #byte out, slave addr, starting memory location on slave

     def setText(self,text):
          self.textCommand(0x01)   # 1 = clear display 
          self.textCommand(0x02)   # 2 = reset cursor to home
          utime.sleep_ms(50)
          self.textCommand(0x08 | 0x04) # display on, no cursor
          self.textCommand(0x28) # 2 lines
          utime.sleep_ms(50)
          count = 0
          row = 0

          for c in text:
               if c == "\n" or count == 16:
                    count = 0
                    row += 1
                    if row == 2:
                         break 
                    self.textCommand(0xC0)
                    if c == "\n":
                         continue
               count += 1
               self.i2c.writeto_mem(TEXT_ADDR, 0x40,c)

screen = GroveRGB_LCD(2)
screen.setRGB(0,255,0)
screen.setText("Hi \nKim")


















