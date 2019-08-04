'''
Vary the potentiometer and see the voltage and temperature on the display

http://wiki.seeedstudio.com/Grove-LCD_RGB_Backlight/

connections: 
Ground (B) - GND 
Power  (R)   - Needs to be 5 volts for the text to work 
SCLK - pin Y9
SDATA -  pin Y10

http://wiki.seeedstudio.com/Grove-Rotary_Angle_Sensor/

connections: 
Ground  - GND 
Power    - 3V3 
NC
Signal -  pin W24

http://wiki.seeedstudio.com/Grove-Temperature_Sensor_V1.2/

connections: 
Ground (B) - GND 
Power  (R)   - 3V3 
NC
Signal -  pin W24

http://wiki.seeedstudio.com/Grove-Buzzer/

connections: 
Ground  - GND 
Power    - 3V3 
NC
Signal -  pin Y9

http://wiki.seeedstudio.com/Grove-Ultrasonic_Ranger/

connections: 
Ground  - GND 
Power    - 3V3 
NC
Signal - pin Y9

http://wiki.seeedstudio.com/Grove-LED_Button/

connections: 
Ground  - GND 
Power    - 3V3 
Signal 2 - button status - pin Y10
Signal1 -  LED status - pin Y9
'''

import GroveClasses.py
import utime

val = GroveAngle('W24')
temp = GroveTemp('W24')
Buzzer = GroveBuzzer('Y9')
sensor = GroveUltrasonic('Y9')
button = GroveLEDBtn(led_pin = 'Y9',btn_pin = 'Y10')
button.on()

screen = GroveRGB_LCD(2)
screen.setRGB(0,255,0)


while True:
     Buzzer.on()
     angle = val.value()/4095.0*360.0)
     print ('%4.2f' % (angle))
     print ('%4.2f' % (temp.value()))
     if button.value():
print('{} cm'.format(sensor.value()))
     screen.setText('%4.2f' % (angle))
     Buzzer.off()
     utime.sleep_ms(200)


'''
######  SPIKE Code #####
import hub,utime

hub.port.B.info()

# if info comes back with None - then you have to restart the pybaord
i=0
fred = bytes([11])
while (i<15):
     try:
          i=i+1 if i<19 else 10
          value = hub.port.B.device.get()[0]
          #print(value)
          hub.display.show(str(value))
          #print(value)
          hub.port.B.device.mode(0,fred*i)
          utime.sleep(0.1)
     except:
          utime.sleep(1)
'''