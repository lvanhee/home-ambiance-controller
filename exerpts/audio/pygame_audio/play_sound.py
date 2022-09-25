import time

from pygame import mixer
import pygame

pygame.init()
mixer.init(channels=5)

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

mixer.music.load("../../../sounds/fanfare.wav")
mixer.music.play()

running = True
while running:
    #for event in pygame.event.get():
    if not pygame.mixer.music.get_busy():
            print('music end event')
            running = False

time.sleep(3)

chan = mixer.find_channel()

sound = mixer.Sound("../../../sounds/test.wav")

sound.play()

sound = mixer.Sound("../../../sounds/test.wav")

sound.play()

print(sound.get_raw())

time.sleep(10)

print("end")