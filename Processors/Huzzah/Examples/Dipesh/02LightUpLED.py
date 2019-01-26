#LED on and off 
#Connect the negative terminal of LED to ground and the positive terminal to Pin 12 
#Use a Resistor 
import machine, time #import library 

ledRed = machine.Pin(12, machine.Pin.OUT) #connect an LED on Pin 12, declare the pin as output 

#ledRed.off() #will turn off the LED

ledRed.on() #will turn on LED 

#Blink LED 
for i in range(5):				#Blink the LED 5 times using a for loop 
	ledRed.on()
	time.sleep_ms(700)			#wait for 700 ms 
	ledRed.off()
	time.sleep_ms(300)			#wait for 300 ms

#Things to try 
#Connect 5 LEDs and create a moving animation from left to right and right to left
#14,12,14,15,0