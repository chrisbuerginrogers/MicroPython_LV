# WS2812 (aka neo pixel) need:
#  - > 4.5v supply
#  - bit freq: between 540kHz and 1540kHz, nominally 800kHz (0.65 - 1.85 us per bit, 1.25 nominal)

import time, machine

class WS2812:
    def __init__(self, spi, n):
        spi.init(baudrate=3_000_000)
        self.spi = spi
        self.buf = bytearray(15 + 9 * n + 1)
        self.buf[-1] = 0xff

    def __len__(self):
        return (len(self.buf) - 16) // 9

    def __setitem__(self, idx, val):
        idx = idx * 9 + 15
        self.fillword(idx, val[1]) # green
        self.fillword(idx + 3, val[0]) # red
        self.fillword(idx + 6, val[2]) # blue

    def write(self):
        self.spi.write(self.buf)

    def fillword(self, idx, val):
        expval = 0
        for i in range(8):
            expval <<= 3
            if val & 0x80:
                expval |= 0b110
            else:
                expval |= 0b100
            val <<= 1
        self.buf[idx] = expval >> 16
        self.buf[idx + 1] = expval >> 8
        self.buf[idx + 2] = expval

def full_test(ws):
    n = len(ws)
    print(n, ws.spi)

    # cycle
    for i in range(4 * n):
        for j in range(n):
            ws[j] = (0, 0, 0)
        ws[i % n] = (255, 255, 255)
        ws.write()
        time.sleep_ms(25)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            ws[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            ws[i % n] = (0, 0, 0)
        else:
            ws[n - 1 - (i % n)] = (0, 0, 0)
        ws.write()
        time.sleep_ms(60)

    # fade in/out
    for i in range(4 * 256):
        for j in range(n):
            if (i // 256) % 2 == 0:
                ws[j] = (i & 0xff, 0, 0)
            else:
                ws[j] = (255 - (i & 0xff), 0, 0)
        ws.write()

    import pyb
    if hasattr(pyb, 'rng'):
        # twinkle
        for i in range(500):
            ws[pyb.rng() % n] = (pyb.rng() % 32, pyb.rng() % 32, pyb.rng() % 32)
            ws[pyb.rng() % n] = (0, 0, 0)
            ws.write()
            time.sleep_ms(5)

    # clear
    for i in range(n):
        ws[i] = (0, 0, 0)
    ws.write()

print('attach WS2812 with at least 8 LEDs to X8 (and GND, 3V3)')
machine.freq(96000000)
ws = WS2812(machine.SPI('X'), 8)
full_test(ws)
