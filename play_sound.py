from playsound import playsound
import time

from pygame import mixer
import pygame

pygame.init()
mixer.init(channels=5)

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

mixer.music.load("hammer.mp3")
mixer.music.play()

running = True
while running:

    #for event in pygame.event.get():
    if not pygame.mixer.music.get_busy():
            print('music end event')
            running = False

time.sleep(3)

chan = mixer.find_channel()

sound = mixer.Sound("hammer.mp3")

sound.play()

time.sleep(3)

print("end")