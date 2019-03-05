import pyb,utime

adc = pyb.ADC('W24')

while True:
     val = adc.read()
     print ('%4.2f' % val)
     utime.sleep_ms(200)
     