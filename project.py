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


trigger0 = 'a'
trigger1 = 's'
trigger2 = 'd'
trigger3 = 'f' # good together
trigger4 = 'g' # good
trigger5 = 'h'
trigger6 = 'r'
trigger7 = 'f'
trigger8 = 't'
trigger9 = 'g'
trigger10 = 'h'

pg.mixer.init()
pg.mixer.set_num_channels(10)

s0 = pg.mixer.Sound('sub_bass.ogg')
s1 = pg.mixer.Sound('bass2.ogg')
s2 = pg.mixer.Sound('drum4.ogg')
s3 = pg.mixer.Sound('melody2.ogg')
s4 = pg.mixer.Sound('drum2.ogg')
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

#channel9.play(s9, loops = -1)
#channel9.set_volume(0.5)
print('working')
while True:
    ball_input = str(input('press a key'))

    if ball_input == trigger0:
        if channel0.get_busy():
            channel0.stop()
        else:
            channel0.play(s0, loops = -1)

    if ball_input == trigger1:
        if channel1.get_busy():
            channel1.stop()
        else:
            channel1.play(s1, loops = -1)

    if ball_input == trigger2:
        if channel2.get_busy():
            channel2.stop()
        else:
            channel2.play(s2, loops = -1)

    if ball_input == trigger3:
        if channel3.get_busy():
            channel3.stop()
        else:
            channel3.play(s3, loops = -1)

    if ball_input == trigger4:
        if channel4.get_busy():
            channel4.stop()
        else:
            channel4.play(s4, loops = -1)

    if ball_input == trigger5:
        if channel5.get_busy():
            channel5.stop()
        else:
            channel5.play(s5, loops = -1)

    #time.sleep(10)

#while mixer.music.get_busy():
#    time.Clock().tick(10)
