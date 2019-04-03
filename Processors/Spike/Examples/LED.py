'''
The user RGB LED capabilities of the hub is a pair of RGB LEDs on 
      either side of the center button.
'''
import hub,utime

hub.led(255, 0, 0) # red  (r,g,b)

hub.led(3) # blue   (colors 0 - 10)

hub.led

for i in range(11):
     hub.led(i)
     utime.sleep(1)
