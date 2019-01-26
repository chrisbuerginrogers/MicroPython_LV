#Connect Huzzah board on your USB port 
#Open Terminal 
#Type: 'ls /dev/tty.*' to see if the board is connected 
#Type: 'screen /dev/tty.SLAB_USBtoUART 115200' to start serial communication 
#On-board LED on and off 
import machine, time #import library 

ledRed = machine.Pin(0, machine.Pin.OUT) #Pin 0 is connected to on board LED, declare the pin as output 

ledRed.off() #will turn off the on board LED

#ledRed.on() #will turn on the on board LED 

#Things to try 
#Connect a Red LED on to other GPIO pins of the board and turn them on and off 
#Can you make the LED blink? 