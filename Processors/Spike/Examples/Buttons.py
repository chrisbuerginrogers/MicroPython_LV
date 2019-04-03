'''
The buttons on the front of the Hub are used to navigate the UI in 
Selection mode, and can be used to interact with the user in the Run mode. 
There are 4 buttons left, center, right, connect
'''

import hub

# can ask if it is currently pressed, was pressed, how many times it has been pressed, and callback

while True:
    if hub.button.left.is_pressed():
        hub.display.show(hub.Image.YES)
    elif hub.button.right.is_pressed():
        hub.display.show(hub.Image.NO)
        
# possible buttons are left, center, right, connect

hub.button.center.is_pressed()  # checks current state of center button

hub.button.center.was_pressed()  # checks if the  center button has been pressed since last checked

hub.button.center.presses()  # returns # presses since last call and rezeros

def smile():
     hub.display.show(hub.Image.SMILE)
     
smile()

#This is not working for me for some reason
hub.button.center.on_change(smile())  # smiles when button pressed

