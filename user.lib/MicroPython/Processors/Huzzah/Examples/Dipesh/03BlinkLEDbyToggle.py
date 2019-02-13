
#Press Ctrl^E to enter paste mode in serial termiinal 
#Press Ctrl^D to run the code

import machine, time

ledRed = machine.Pin(0, machine.Pin.OUT)

ledRed.on()			#turn on LED
ledRed.off()		#turn off LED

def toggle(l):
	l.value(not l.value())	#change value of led

while True:
	toggle(ledRed)				#toggle ledRed on and off 
	time.sleep_ms(500)			#wait for 500 ms

