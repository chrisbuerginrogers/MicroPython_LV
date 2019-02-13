import machine, utime

led = machine.Pin(0, machine.Pin.OUT)


for i in range(5):
     led.value(0)
     utime.sleep_ms(1000)
     led.value(1)
     utime.sleep_ms(1000)


