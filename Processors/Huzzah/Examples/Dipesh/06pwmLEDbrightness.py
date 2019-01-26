#PWM can be enabled on all pins expect Pin 16 

import machine, time #import library 

led12 = machine.PWM(machine.Pin(12)) #Enable PWM in Pin 12

led12.freq(60)			#Set the pwm frequency to 60 Hz 

led12.duty(0)		#LED completely off 
led12.duty(512)		#LED with mid brightness
led12.duty(1023)	#LED with maximum brightness 

for i in range(1024):		#change from dim to bright 
	led12.duty(i)
	time.sleep_ms(10)

for i in range(1023,-1,-1): #change from bright to dim 
	led12.duty(i)
	time.sleep_ms(10)
	print(i)




