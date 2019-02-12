import machine

pwm = machine.PWM(machine.Pin(15))
pwm.freq(50)


pwm.duty(506)

