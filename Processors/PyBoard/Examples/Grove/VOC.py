import pyb,utime

i2c = pyb.I2C(2,pyb.I2C.MASTER)
i2c.scan()
#should see an 88

#then a lot oof complicated stuff...
