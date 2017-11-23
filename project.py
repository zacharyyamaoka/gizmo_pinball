import pygame as pg
import random
import time

pg.mixer.init()
sound = pg.mixer.Sound('edx.wav')
channel1 = pg.mixer.Channel(0)
channel1.play(sound, loops = -1)

while True:
    time.sleep(10)
#while mixer.music.get_busy():
#    time.Clock().tick(10)
