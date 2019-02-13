# Getting Started

# Try typing
print('this is a test, this is only a test') # in the REPL and you should see it printed as a reply.

#You can type math - try

2 + 2

# If you type more than one line, spaces are important - for instance if you define a function:

def Tell():
     print('more testing')

# and then call the function

Tell()   # and you should see the text printed.



# To run existing code in libraries, you have to "import".  Try getting a directory listing with:

import os
os.listdir()    #and you should get an array of text strings returned.

#https://docs.micropython.org/en/latest/index.html

#-------------------------Loops

# There are many different kinds.  The standard for loop going from 0 to 9 is just

for i in range(10):
     print (i)

# You can also pull from a list:

for i in[1,3,5,9]:
     print (i)

# or run until a condition is met:

i = 0
while i < 10:
     print (i) 
     i = i + 1

#or run forever:

import utime
i = 0
while True:
     print (i) 
     i = i + 1
     utime.sleep(1)  # wait one second between prints so that you can hit CTRL-C and continue on

#------------------------- Conditionals

#You can have a standard if..then..else format:

A=3
B=1
def Test():
     if A < B:
         print ('A Wins')
     else:
         if B:
             for i in ["1","3","5"]:
                 print ('i=',i)
         else:
             print ('B Loses')
             
Test()


#------------------------- Running code that might not work...

# Use the "Try: Except:" options.  A sample would be

from pyb import SPI
spi = SPI(2, SPI.SLAVE, polarity=0, phase=0)
spi.MSB

data=bytearray(4)
reply=bytearray(4)
data[0]=2
data[1]=1
data[2]=3
data[3]=11

def Test():
     try:
          spi.send_recv(data,reply)
          print(reply)
     except:
          print('failed')

Test()


