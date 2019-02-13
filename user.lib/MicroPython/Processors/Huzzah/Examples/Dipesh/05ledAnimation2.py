import machine, time #import library 

led = ['led1','led2','led3','led4','led5'] #list of LEDs being used 
led[0] = machine.Pin(14, machine.Pin.OUT)
led[1] = machine.Pin(12, machine.Pin.OUT)
led[2] = machine.Pin(13, machine.Pin.OUT)
led[3] = machine.Pin(15, machine.Pin.OUT)
led[4] = machine.Pin(16, machine.Pin.OUT)

#Turn on all LEDs 
def TurnAllLEDon():
	for i in range(5):
		led[i].on()

#Turn on all LEDs 
def TurnAllLEDoff():
	for i in range(5):
		led[i].off()

#Animate LEDs from left to right 
def leftToRight(times):
	for count in range(times):		#Animate the LED x times using a for loop 
		for i in range(5):			#From 0 to 4, 5 is out of range 	
			led[i].on()
			time.sleep_ms(300)
			led[i].off()
		
#Animate LEDs from right to left 
def rightToLeft(times):
	for count in range(times):		#Animate the LED x times using a for loop 
		for i in range(4,-1,-1):	#From 4 to 0, -1 is out of range  			
			led[i].on()
			time.sleep_ms(300)
			led[i].off()


def main():
	#TurnAlLEDon()			#Turn on all LEDs
	#TurnAlLEDoff()			#Turn off all LEDs
	#leftToRight(3)			#Animate LEDs from left to right
	rightToLeft(3)			#Animate LEDs from right to left 

if __name__ == '__main__':
	main()

#Things to try 
#Create a 5 bit binary counter using the LEDs