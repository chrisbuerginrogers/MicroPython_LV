'''
http://wiki.seeedstudio.com/Grove-Temperature_and_Humidity_Sensor_Pro/

connections: 
Ground  - GND 
Power    - 3V3 
NC
Signal -  pin Y10
'''


import dht
import machine, utime
#DHT library from website 
d=dht.DHT11(machine.Pin('Y10'))

while True:
     d.measure()
     print("Temp:")
     print(d.temperature())
     print("Humidity:")
     print(d.humidity())
     utime.sleep_ms(500)


