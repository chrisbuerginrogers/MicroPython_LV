import machine, time #import library 

led1 = machine.Pin(14, machine.Pin.OUT)
led2 = machine.Pin(12, machine.Pin.OUT)
led3 = machine.Pin(13, machine.Pin.OUT)
led4 = machine.Pin(15, machine.Pin.OUT)
led5 = machine.Pin(16, machine.Pin.OUT)

#Turn on all LEDs 
def TurnAllLEDon():
	led1.on() #will turn on LED on Pin 14 
	led2.on()
	led3.on()
	led4.on()
	led5.on()

#Turn on all LEDs 
def TurnAllLEDoff():
	led1.off() #will turn of LED on Pin 14 
	led2.off()
	led3.off()
	led4.off()
	led5.off()

def leftToRight(times):
	for i in range(times):				#Animate the LED x times using a for loop 
		led1.on()
		time.sleep_ms(300)
		led1.off()
		led2.on()
		time.sleep_ms(300)
		led2.off()
		led3.on()
		time.sleep_ms(300)
		led3.off()
		led4.on()
		time.sleep_ms(300)
		led4.off()
		led5.on()
		time.sleep_ms(300)
		led5.off()
		


def main():
	#TurnAlLEDon()
	#TurnAlLEDoff()
	leftToRight(3)


if __name__ == '__main__':
	main()

#Things to try 
#Animate the LED from right to left 
#simplify the function leftToRight(times) 
