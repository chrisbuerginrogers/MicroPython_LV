'''
https://github.com/sparkfunX/Qwiic_Joystiick
     
Black - GND
Red - 3V3
Blue - SCL - Y10
Yellow - SDA - Y9
'''

import machine,utime

i2c = machine.I2C(2)
i2c.scan()
#should see an 32 (0x20)

while True:
     try:
          data = bytearray(i2c.readfrom_mem(32,3,5))
          Hpos = (data[0]<<8 | data[1])>>6
          Vpos =  (data[2]<<8 | data[3])>>6
          Btn = data[4]
          print( 'H: %4d   V:%4d   Btn %2d' % (Hpos,Vpos,Btn))
               
     except Exception as e:
          print(e)
     utime.sleep_ms(200)

'''
######  SPIKE Code #####
import hub,utime

hub.port.B.info()

# if info comes back with None - then you have to restart the pybaord
i=0
fred = bytes([11])
while True:
     try:
          i=i+1 if i<9 else 0
          value = hub.port.B.device.get()[0]
          #print(value)
          hub.display.show(str(value))
          #print(value)
          #hub.port.B.device.mode(0,fred*i)
          utime.sleep(0.1)
     except:
          utime.sleep(1)
'''