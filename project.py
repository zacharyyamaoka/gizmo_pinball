import pygame as pg
#from gpiozero import
import random
import time
'''input0 =
input0 =
input0 =
input0 =
input0 =
input0 =
input0 = '''


trigger0 = 'q'
trigger1 = 'w'
trigger2 = 'e'
trigger3 = 'a'
trigger4 = 's'
trigger5 = 'd'
trigger6 = 'r'
trigger7 = 'f'
trigger8 = 't'
trigger9 = 'g'
trigger10 = 'h'

pg.mixer.init()
pg.mixer.set_num_channels(10)

s0 = pg.mixer.Sound('edx.wav')
s1 = pg.mixer.Sound('bass.wav')
s2 = pg.mixer.Sound('drum1.wav')
s3 = pg.mixer.Sound('edx.wav')
s4 = pg.mixer.Sound('edx.wav')
s5 = pg.mixer.Sound('edx.wav')
s6 = pg.mixer.Sound('edx.wav')
s7 = pg.mixer.Sound('edx.wav')
s8 = pg.mixer.Sound('edx.wav')
s9 = pg.mixer.Sound('edx.wav')

channel0 = pg.mixer.Channel(0)
channel1 = pg.mixer.Channel(1)
channel2 = pg.mixer.Channel(2)
channel3 = pg.mixer.Channel(3)
channel4 = pg.mixer.Channel(4)
channel5 = pg.mixer.Channel(5)
channel6 = pg.mixer.Channel(6)
channel7 = pg.mixer.Channel(7)
channel8 = pg.mixer.Channel(8)
channel9 = pg.mixer.Channel(9)

#channel1.play(s0, loops = -1)
print('working')
while True:
    ball_input = str(input('press a key'))

    if ball_input == trigger0:
        if channel0.get_busy():
            channel0.stop()
        else:
            channel0.play(s0, loops = -1)

    if ball_input == trigger2:
        if channel2.get_busy():
            channel2.stop()
        else:
            channel2.play(s1, loops = -1)



    #time.sleep(10)

#while mixer.music.get_busy():
#    time.Clock().tick(10)
