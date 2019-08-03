'''
http://wiki.seeedstudio.com/

'''

from pyb import ADC, Pin,time_pulse_us
from machine import I2C
import utime

class GroveButton(object):
    def __init__(self, pin):
         self.button = Pin(pin,Pin.IN)

    def value(self):
        return self.button.value()
        
class GroveAngle(object):
    def __init__(self, pin):
         self.adc = ADC(pin)

    def value(self):
        return self.adc.read()
        
class GroveLEDBtn(object):
    def __init__(self, btn_pin,led_pin):
         self.btn = Pin(btn_pin,Pin.IN)
         self.led = Pin(led_pin,Pin.OUT)

    def value(self):
        return self.btn.value()

    def toggle(self):
        self.led.value(not self.led.value())
        
    def on(self):
         self.led.value(True)
        
    def off(self):
         self.led.value(False)

class GroveRelay(object):
    def __init__(self, pin):
         self.relay = Pin(pin,Pin.OUT)

    def value(self):
        return self.relay.value()

    def toggle(self):
        self.relay.value(not self.relay.value())

    def on(self):
         self.relay.value(True)
        
    def off(self):
         self.relay.value(False)

class GroveLight(object):
    def __init__(self, pin):
         self.adc = ADC(pin)

    def value(self):
        return self.adc.read()
        
class GroveUltrasonic(object):
    def __init__(self, pin):
         self.dio = Pin(pin)

     def value(self):
          dt=-1
          while dt<0:
               self.dio.init(Pin.OUT)
               self.dio.value(0)
               utime.sleep_us(2)
               self.dio.value(1)
               utime.sleep_us(10)
               self.dio.value(0)
               self.dio.init(Pin.IN)
               dt = time_pulse_us(self.dio, 1, 100000)

          return  (dt / 29 / 2)    # cm
          
class GroveBuzzer(object):
    def __init__(self, pin):
         self.buzz = Pin(pin,Pin.OUT)

    def value(self):
        return self.buzz.value()

    def toggle(self):
        self.buzz.value(not self.buzz.value())

    def on(self):
         self.buzz.value(True)
        
    def off(self):
         self.buzz.value(False)
         
charmap = {
    '0': 0x3f,'1': 0x06,'2': 0x5b,'3': 0x4f,'4': 0x66,'5': 0x6d,'6': 0x7d,'7': 0x07,'8': 0x7f,
    '9': 0x6f,'A': 0x77,'B': 0x7f,'b': 0x7C,'C': 0x39,'c': 0x58,'D': 0x3f,'d': 0x5E,'E': 0x79,
    'F': 0x71,'G': 0x7d,'H': 0x76,'h': 0x74,'I': 0x06,'J': 0x1f,'K': 0x76,'L': 0x38,'l': 0x06,
    'n': 0x54,'O': 0x3f,'o': 0x5c,'P': 0x73,'r': 0x50,'S': 0x6d,'U': 0x3e,'V': 0x3e,'Y': 0x66,
    'Z': 0x5b,'-': 0x40,'_': 0x08,' ': 0x00}

ADDR_AUTO = 0x40
ADDR_FIXED = 0x44
STARTADDR = 0xC0
BRIGHT_DARKEST = 0
BRIGHT_DEFAULT = 2
BRIGHT_HIGHEST = 7

class Grove4Digit(object):
    def __init__(self, clk,dio):
         self.clk = Pin(clk,Pin.OUT,Pin.PULL_UP)
         self.dio = Pin(dio,Pin.OUT,Pin.PULL_UP)

    def value(self):
        return self.button.value()

     def start(self):
          self.clk.value(1)
          self.dio.value(1)
          self.dio.value(0)
          self.clk.value(0)
     
     def stop(self):
          self.clk.value(0)
          self.dio.value(0)
          self.clk.value(1)
          self.dio.value(1)
     
     def writeByte(self,data):
          for _ in range(8):
               self.clk.value(0)
               if data & 0x01:
                    self.dio.value(1)
               else:
                    self.dio.value(0)
               data >>= 1
               utime.sleep_us(1)
               self.clk.value(1)
               utime.sleep_us(1)

          self.clk.value(0)
          self.dio.value(1)
          self.clk.value(1)
          self.dio.init(Pin.IN,Pin.PULL_UP)
          utime.sleep_ms(50)
          ack = self.dio.value()
          if (ack == 0):
               self.dio.init(Pin.OUT,Pin.PULL_UP)
               self.dio.value(0)
          utime.sleep_ms(50)
          self.dio.init(Pin.OUT,Pin.PULL_UP)
          utime.sleep_ms(50)
     
     def display(self,data,brightness=BRIGHT_DEFAULT,colon=False):
          self.start()
          self.writeByte(ADDR_AUTO)
          self.stop()
     
          self.start()
          self.writeByte(STARTADDR)
          if len(data) < 4:
               data = data + '    '
          for i in range(4):
               self.writeByte(charmap[data[i]] | 0x80 * colon)
          self.stop()
     
          if brightness > BRIGHT_HIGHEST:
               brightness = BRIGHT_HIGHEST
          if brightness < BRIGHT_DARKEST:
               brightness = BRIGHT_DARKEST
          self.start()
          self.writeByte(0x88 +  brightness)
          self.stop()
     
     def clear(self):
          self.display('    ',4,0)
          
GLB_CMDMODE = 0x00  # Work on 8-bit mode
MAX_BRIGHTNESS = 0xFF

class GroveLEDBar(object):
     def __init__(self, dio,clk,RtoG=True):
          self.dio = Pin(dio, Pin.OUT,Pin.PULL_UP)
          self.clk = Pin(clk, Pin.OUT,Pin.PULL_UP)
          self.RtoG = RtoG
          self.stateArray = bytearray(10)
          for i in range(10):
               self.stateArray[i] = 0x00  # allows me to toggle individual elements

     def sendData(self,data):
          state = 0
          for i in range(16):
               state1 = (data & 0x8000)
               self.dio.value(state1)
               state=1-state
               self.clk.value(state)
               data<<=1
          
     def latchData(self):
          self.dio.value(0)
          utime.sleep_ms(10)
          for i in range(4):
               self.dio.value(1)
               utime.sleep_us(1)
               self.dio.value(0)
               utime.sleep_us(1)
          
     def setData(self):
          self.sendData(GLB_CMDMODE)
          for i in range(10):
               self.sendData(self.stateArray[i])
               
          self.sendData(0x00)  
          self.sendData(0x00)
          self.latchData()
          
     def setBits(self,bits):
          for  i in range(10):
               if self.RtoG:
                    j = i
               else:
                    j = 9-i
               if ((bits % 2) == 1):
                    self.stateArray[j] = MAX_BRIGHTNESS
               else:
                    self.stateArray[j] = 0x00
               bits = int(bits / 2)
          self.setData()

     def setBrightness(self,led,brightness):
          led = min(9,max((led-1),0))
          brightness = min (1,max(brightness,0))
          if ~self.RtoG:
               led = 9-led
          self.stateArray[led] =0xFF & ~(~0<< int(8*brightness))
          self.setData()

     def toggleLED(self,led):
          led = min(9,max((led-1),0))
          if ~self.RtoG:
               led = 9-led
          self.stateArray[led] = ~ self.stateArray[led]
          self.setData()
          
     def meter(self,value):
          value = min(10,max(value,0))
          self.setBits(-1 + 2**value)
         
class GroveTemp(object):
     def __init__(self, pin):
          self.adc = ADC(pin)

     def value(self):
          B = 4275             # B value of the thermistor
          R0 = 100000      #R0 = 100k 
          val = adc.read()
          R = 4095/val-1.0
          R = R0*R
          temperature = 1.0/(math.log10(R/R0)/B+1/298.15)-273.15 
          
class GroveSPL(object):
     def __init__(self, pin):
          self.adc = ADC(pin)

     def value(self):
          val = 0
          for i in range (100):
               val = val + self.adc.read()
          val = val / 100
          return val
          
class GroveAirQuality(object):

     def __init__(self, pin):
          self.adc = ADC(pin)

     @property
     def value(self):
          return self.adc.read() / 4096 * 1024
          
class GroveRGB_LCD(object):
     def __init__(self, i2c):
          self.i2c = I2C(i2c)
          self.TEXT_ADDR = 0x3E   #62
          self.RGB_ADDR = 0x62    #98

     def setRGB(self,r,g,b):
          self.i2c.writeto_mem(self.RGB_ADDR, 0x00,b'\x00')
          self.i2c.writeto_mem(self.RGB_ADDR, 0x01,b'\x00')
          self.i2c.writeto_mem(self.RGB_ADDR, 0x08,b'\xAA')
          self.i2c.writeto_mem(self.RGB_ADDR, 0x04, chr(r))
          self.i2c.writeto_mem(self.RGB_ADDR, 0x03,  chr(g))
          self.i2c.writeto_mem(self.RGB_ADDR, 0x02,  chr(b))

     def textCommand(self,cmd):
          self.i2c.writeto_mem(self.TEXT_ADDR, 0x80, chr(cmd)) #byte out, slave addr, starting memory location on slave

     def setText(self,text):
          self.textCommand(0x01)   # 1 = clear display 
          self.textCommand(0x02)   # 2 = reset cursor to home
          utime.sleep_ms(50)
          self.textCommand(0x08 | 0x04) # display on, no cursor
          self.textCommand(0x28) # 2 lines
          utime.sleep_ms(50)
          count = 0
          row = 0

          for c in text:
               if c == "\n" or count == 16:
                    count = 0
                    row += 1
                    if row == 2:
                         break 
                    self.textCommand(0xC0)
                    if c == "\n":
                         continue
               count += 1
               self.i2c.writeto_mem(TEXT_ADDR, 0x40,c)

          return temperature