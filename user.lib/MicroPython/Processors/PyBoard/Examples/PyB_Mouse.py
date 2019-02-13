#from https://github.com/micropython/micropython/blob/master/docs/pyboard/tutorial/usb_mouse.rst


# Add to boot.py
import pyb
pyb.usb_mode('VCP+HID') # act as a serial device and a mouse

# Move it
hid = pyb.USB_HID()
hid.send((0, 10, 0, 0))

# Oscillate
import math
def osc(n, d):
   for i in range(n):
   hid.send((0, int(20 * math.sin(i / 10)), 0, 0))
   pyb.delay(d)

osc(100, 50)

# Connect to accel - NOTE you will need to use safe mode to stop - see webapge
import pyb

switch = pyb.Switch()
accel = pyb.Accel()
hid = pyb.USB_HID()

while not switch():
    hid.send((0, accel.x(), accel.y(), 0))
    pyb.delay(20)

#Safe Mode

#Hold down the USR switch.
#While still holding down USR, press and release the RST switch.
#The LEDs will then cycle green to orange to green+orange and back again.
#Keep holding down USR until only the orange LED is lit, and then let go of the USR switch.
#The orange LED should flash quickly 4 times, and then turn off.
#You are now in safe mode.
