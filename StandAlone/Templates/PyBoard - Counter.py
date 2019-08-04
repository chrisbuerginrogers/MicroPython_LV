import gc,utime
import pyb, micropython
import LPF2Class

micropython.alloc_emergency_exception_buf(200)

# Name, Format [# datasets, type, figures, decimals], raw [min,max], Percent, SI, Symbol,functionMap, view
mode0 = ['LPF2-DETECT',[1,LPF2Class.DATA8,3,0],[0,10],[0,100],[0,10],'',[LPF2Class.ABSOLUTE,0],True]
mode1 = ['LPF2-COUNT',[1,LPF2Class.DATA32,4,0],[0,100],[0,100],[0,100],'CNT',[LPF2Class.ABSOLUTE,0],True]
mode2 = ['LPF2-CAL',[3,LPF2Class.DATA16,3,0],[0,1023],[0,100],[0,1023],'RAW',[LPF2Class.ABSOLUTE,0],False]
modes = [mode0,mode1,mode2]

red_led=pyb.LED(1)
green_led = pyb.LED(2)
red_led.on()

lpf2 = LPF2Class.LPF2(1, 'Y1', 'Y2', modes, type = LPF2Class.WeDo_Ultrasonic, timer = 4, freq = 5)    # PyBoard
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