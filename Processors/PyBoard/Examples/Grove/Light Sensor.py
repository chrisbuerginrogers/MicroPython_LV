import pyb,utime

Light = pyb.ADC('W24')

while True:
     Light.read()
     utime.sleep_ms(200)