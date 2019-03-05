# http://wiki.seeedstudio.com/Grove-OLED_Display_1.12inch/

import pyb,utime

PIR = pyb.Pin('Y9', pyb.Pin.IN)

PIR.value()

while True:
     PIR.value()
     utime.sleep_ms(200)