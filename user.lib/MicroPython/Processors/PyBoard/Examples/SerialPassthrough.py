from pyb import UART
import utime,math
import lcd160cr, machine, utime

lcd = lcd160cr.LCD160CR("Y")
lcd.set_orient(lcd160cr.LANDSCAPE)
lcd.set_startup_deco(lcd160cr.STARTUP_DECO_MLOGO)
lcd.set_brightness(10)
lcd.erase()
lcd.set_pos(0, 0)
lcd.set_text_color(lcd.rgb(255, 255, 255), lcd.rgb(0, 0, 0))
lcd.set_font(2)
lcd.set_pos(0, 0)
lcd.write("Code Check\r\n")

uart=UART(1)
uart.init(9600, bits=8, parity=None, stop=1) 

uart2=UART(4)
uart2.init(9600, bits=8, parity=None, stop=1) 

while True:
     if uart.any():       
          incoming = uart.read()
          lcd.write(">> " + str(incoming) +"\r\n")
          uart2.write(incoming)
     if uart2.any():
          incoming = uart2.read()
          uart.write(incoming)
          lcd.write("<< " + str(incoming) +"\r\n")