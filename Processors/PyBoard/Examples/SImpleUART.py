import time,pyb

uart = pyb. UART(3,9600, bits=8, parity=None, stop=1)

while(True):
    time.sleep_ms(100)
    size = uart.any()
    if (size > 0):
        string = uart.read(size)
        data = int(string[-1])
        print('Data: %3d' % (data))


