'''
http://wiki.seeedstudio.com/Grove-16-Channel_PWM_Driver-PCA9685/

connections: 
Ground  - GND 
Power    - 3V3 
SCLK - pin Y9
SDATA -  pin Y10
'''

import pyb,utime

i2c = pyb.I2C(2,pyb.I2C.MASTER)
i2c.scan()
# should see 0x7F - but am seeing 0x70 for some reason
MODE1     =    0x00
MODE2     =    0x01
LED0_ON_L       =  0x06
ALL_LED_ON_L =    0xfa
PRESCALE        =  0xfe

SLEEP       = 0x10
EXTCLK    =  0x40  
RESTART  =   0x80 
ADDR =   0x7f

SERVO_MIN = 500     #  min pulse is 0.5 ms
SERVO_MAX = 2500  #  max pulse is 2.5 ms
ANGLE_MAX = 180
CALIB = ((SERVO_MAX-SERVO_MIN)/ANGLE_MAX)+SERVO_MIN

def restart():
     i2c.mem_write(RESTART,ADDR,MODE1)
     utime.sleep_ms(10)
     i2c.mem_write(SLEEP,ADDR,MODE1)  # sleep internal oscillator
     utime.sleep_ms(2)
     i2c.mem_write((EXTCLK | SLEEP),ADDR,MODE1) # enable external oscillator
     utime.sleep_ms(2)
     i2c.mem_write(0x00,ADDR,MODE1)  # turn on oscillator
     utime.sleep_ms(2)
     
def led_init():
     restart()
     setFrequency(100)
     
def servo_init():
     restart()
     setFrequency(50)
     
def setFrequency(freq):
     if (freq<24):
          freq = 24
     if (freq > 1526):
          freq = 1526
     val = (25000000.0/4096.0)/freq - 1
     prescale = 0xFF & int(val + 0.5)
     buffer = i2c.mem_read(1,ADDR,MODE1)
     i2c.mem_write(((ord(buffer) & 0x7F) | SLEEP),ADDR,MODE1)
     utime.sleep_ms(2)
     i2c.mem_write(prescale,ADDR,PRESCALE)
     i2c.mem_write(buffer,ADDR,MODE1)
     utime.sleep_ms(2)
     i2c.mem_write((ord(buffer) | 0xA0),ADDR,MODE1)
     utime.sleep_ms(2)
     
def setAngle(pin,angle):
     if (angle < ANGLE_MAX):
          angle = ANGLE_MAX
     min = (2.46 * SERVO_MIN)/10.0 - 1
     max = (2.46 * SERVO_MAX)/10.0 - 1
     setPWM(pin,0, int(angle * CALIB))
     
def setPWM(pin,led_on,led_off):
     if (pin < 1):
          pin = 1
     if (pin>16):
          pin = 16
     buffer = bytearray(4)
     buffer[0] = led_on & 0xFF
     buffer[1] = led_on >> 8
     buffer[2] = led_off & 0xFF
     buffer[3] = led_off >> 8
     i2c.mem_write(buffer,ADDR,(LED0_ON_L+4*(pin-1)))
     
     
servo_init()

setAngle(1,0)
utime.sleep_ms(1000)
setAngle(1,90)
utime.sleep_ms(1000)

