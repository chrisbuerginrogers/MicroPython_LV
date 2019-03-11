'''
http://wiki.seeedstudio.com/Grove-Temperature_Sensor_V1.2/

connections: 
Ground (B) - GND 
Power  (R)   - 3V3 
NC
Signal -  pin W24
'''

import pyb,utime,math

B = 4275             # B value of the thermistor
R0 = 100000      #R0 = 100k

adc = pyb.ADC('W24')

while True:
     val = adc.read()
     R = 4095/val-1.0
     R = R0*R
     temperature = 1.0/(math.log10(R/R0)/B+1/298.15)-273.15 
# convert to temperature via datasheet - Celsius
     print ('Temperature: %4.2f' % temperature)
     utime.sleep_ms(200)
     







