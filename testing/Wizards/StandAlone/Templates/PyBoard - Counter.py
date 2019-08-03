import gc,utime
import pyb, micropython
from LPF2Class import LPF2

micropython.alloc_emergency_exception_buf(200)

red_led=pyb.LED(1)
green_led = pyb.LED(2)
red_led.on()

lpf2 = LPF2(1, 'Y1', 'Y2', timer = 4, freq = 5)    # PyBoard
lpf2.initialize()

value = 0

# Loop
while True:
     if not lpf2.connected:
          lpf2.sendTimer.callback(None)
          red_led.on()
          utime.sleep_ms(200)
          lpf2.initialize()
     else:
          red_led.off()
          lpf2.load_payload(value)
          value = value + 1 if value <9 else 0
          data = lpf2.readIt(timeout = 0.01)


          utime.sleep_ms(90)

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