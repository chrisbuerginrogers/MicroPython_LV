# http://wiki.seeedstudio.com/Grove-OLED_Display_1.12inch/

import pyb,utime

i2c = pyb.I2C(2,pyb.I2C.MASTER)
i2c.scan()
#should see an 60
