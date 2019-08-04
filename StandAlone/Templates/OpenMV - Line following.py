import LPF2Class
import sensor, image, time

enable_lens_corr = False # turn on for straighter lines...

sensor.reset()
sensor.set_pixformat(sensor.RGB565) # grayscale is faster
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)

min_degree = 0
max_degree = 179


red_led.on()
lpf2 = LPF2Class.LPF2(1, 'P1', 'P0')    # OpenMV
lpf2.connected = True
#lpf2.initialize()

while True:
     img = sensor.snapshot()
     if enable_lens_corr: img.lens_corr(1.8) # for 2.8mm lens...
          
     if not lpf2.connected:
          red_led.on()
          utime.sleep(1)
          lpf2.initialize()
     else:
          red_led.off()
          while lpf2.connected:
               gc.collect()
               rawLines = img.find_lines(threshold = 1000, theta_margin = 25, rho_margin = 25)
               averageAngle = 0
               for line in rawLines:
                    if (min_degree <= line.theta()) and (line.theta() <= max_degree):
                         img.draw_line(line.line(), color = (255, 0, 0))
                         averageAngle + = line.theta()
               value = averageAngle / len(rawLines)

               lpf2.send_value(value)
               print(value)
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