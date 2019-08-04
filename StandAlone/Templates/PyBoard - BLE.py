import bluetooth
bt = bluetooth.Bluetooth()
bt.active(True)

LPF2_SERVICE = bluetooth.UUID('00001623-1212-EFDE-1623-785FEABCD123')
LWP_CHAR = (bluetooth.UUID('00001624-1212-EFDE-1623-785FEABCD123'), bluetooth.FLAG_NOTIFY|bluetooth.FLAG_WRITE,)
lwp_char, = bt.gatts_add_service(LPF2_SERVICE, (LWP_CHAR,))

bt.advertise(100, adv_data=bytearray('\x02\x01\x02\x0a\x09pybd-lpf2'))



#Now to send data from pyboard->hub do:

bt.gatts_notify(lwp_char, 64, 'from pybd')

#Then on pyboard get this data via:

bt.gatts_read(lwp_char)

# You can also register IRQ callbacks on the pyboard for all BLE events, like this:

'''
def bt_irq(event, data):
    print('bt_irq', event, data)
bt.irq(bt_irq, bluetooth.IRQ_ALL)

'''

'''
######  SPIKE Code #####
import hub,utime

hub.ble.scan(10)

utime.sleep(10)
hub.ble.scan_result()

# wait a few seconds
p = hub.ble.connect(0) # hopefully index 0 is the pyboard, if not you'll have to find the right index via hub.ble.scan_result()

# {'service_id': '232004FD-4200-0032-6670-6C2D64627970', 'rssi': -16, 'man_data': b'\x00\x00\x80\x98m\x9a', 'mac_addr': '48:4A:30:01:9A:C2', 'man_id': 227}


p.callback(lambda data:print(data))
p.subscribe()

p.send('from hub')

p = hub.ble.connect(1)
'''