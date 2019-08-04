'''
The sound capabilities of the hub are currently limited to generating 
     simple waveforms:

sin
square
triangle
sawtooth

The volume of the speaker in the low frequency range (800 Hz) is limited
'''

import hub,utime

hub.sound.volume()
hub.sound.volume(10)  # 0 - 10 
hub.sound.beep()
hub.sound.beep(2000, 500, 3)  # freq, time, waveform (sin,square,triangle, sawtooth

# can also play files and have a callback when the sound is complete or interrupted
