import pyb,utime

Relay = pyb.Pin('Y10', pyb.Pin.OUT)

Relay.on()
utime.sleep_ms(200)
Relay.off()

