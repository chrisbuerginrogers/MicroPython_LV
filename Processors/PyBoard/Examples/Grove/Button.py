import pyb,utime

button = pyb.Pin('W16')

button()
utime.sleep(10)
button()
