#fromhttps://github.com/micropython/micropython/blob/master/docs/pyboard/tutorial/fading_led.rst

rom pyb import Timer
from time import sleep

# timer 5 will be created with a frequency of 100 Hz
tim = pyb.Timer(5, freq=100)
tchannel = tim.channel(1, Timer.PWM, pin=pyb.Pin.board.X1, pulse_width=0)


#-------- Fading LED

# maximum and minimum pulse-width, which corresponds to maximum
# and minimum brightness
max_width = 200000
min_width = 20000

# how much to change the pulse-width by each step
wstep = 1500
cur_width = min_width

while True:
  tchannel.pulse_width(cur_width)
  # this determines how often we change the pulse-width. It is
  # analogous to frames-per-second
  sleep(0.01)
  cur_width += wstep
  if cur_width > max_width:
    cur_width = min_width

#---------- Breathing LED

while True:
  tchannel.pulse_width(cur_width)
  sleep(0.01)
  cur_width += wstep
  if cur_width > max_width:
    cur_width = max_width
    wstep *= -1
  elif cur_width < min_width:
    cur_width = min_width
    wstep *= -1
