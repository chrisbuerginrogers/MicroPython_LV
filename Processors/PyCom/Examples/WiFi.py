'''
https://docs.pycom.io/tutorials/all/wlan.html
'''

import machine
from network import WLAN
wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()

nets

for net in nets:
    if net.ssid == 'HighPeaks':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'password'), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break