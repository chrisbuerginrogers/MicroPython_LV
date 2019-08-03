# Track blobs

import LPF2Class,gc,utime
import sensor, image
import pyb

red_led=pyb.LED(1)
green_led = pyb.LED(2)
red_led.on()
lpf2 = LPF2Class.LPF2(3, 'P4', 'P5')    # OpenMV

# Setup
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False) 

lpf2.connected = False
value = 0
# Loop
while True:
     if not lpf2.connected:
          red_led.on()
          utime.sleep_ms(200)
          lpf2.initialize()
     else:
          red_led.off()
          green_led.off()
          gc.collect()
          lpf2.send_value(value)
          img = sensor.snapshot()
          junk = img.lens_corr(1.8) # strength of 1.8 is good for the 2.8mm lens.
          qr_codes = img.find_qrcodes()
          if len(qr_codes) == 0:
               value = -1
          else:
               green_led.on()
               for code in qr_codes:
                    img.draw_rectangle(code.rect(), color = (255, 0, 0))
                    data = int(code[4])
                    value = data
                    
                    
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