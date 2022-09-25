import os
from pygame import mixer
import pygame
import time
pygame.init()
mixer.init(channels=5)

def stop_all_sounds():
    os.system("START syrinscape-fantasy:stop-all/")
    #os.system("START syrinscape-boardgame:moods/dHJhaW4tZ2FtZXMtaWk6OkJ1c3kgZGF5IG9uIHRoZSByYWlscw/play/")

def play_sound(filename, blocking):
    mixer.music.load(filename)
    mixer.music.play()
    if(blocking):
        while mixer.music.get_busy():
            time.sleep(1)