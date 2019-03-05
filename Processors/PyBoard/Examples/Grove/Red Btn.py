import pyb,utime

Btn = pyb.Pin('Y9', pyb.Pin.IN)
LED = pyb.Pin('Y10', pyb.Pin.OUT)

Btn.value()

def btn_callback(line):
        if LED.value():
             LED.off()
        else:
             LED.on()

Btn_interrupt = pyb.ExtInt(Btn, pyb.ExtInt.IRQ_FALLING, pyb.Pin.PULL_NONE, btn_callback)
