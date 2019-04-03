'''
The ports on the hub are able to autodetect the capabilities of 
     the device that is plugged in. \When a motor device is detected, 
     then an enhanced set of methods is available.
'''

import hub,utime

hub.port.A.motor.mode(1)
hub.port.A.motor.get()
hub.port.A.motor.pwm(100) # from -100 to 100
utime.sleep(1)
hub.port.A.motor.float()
hub.port.A.motor.brake()
hub.port.A.motor.run_at_speed(speed = 50, max_power = 100, acceleration = 100, deceleration = 100, stall = False)
hub.port.A.motor.run_for_degrees(degrees = 90, speed = 50)
hub.port.A.motor.run_to_position(90, 50)  # position and speed
hub.port.A.motor.default()
hub.port.A.motor.run_for_time(100, 50)   # time - msec and speed


hub.port.B.info()

# only works if motors are connected
p = hub.port.A.motor.pair(hub.port.B.motor)
p.pwm(40,-40)   # drive straight
p.run_for_time(200,40,-40)
p.float()   # not working yet
