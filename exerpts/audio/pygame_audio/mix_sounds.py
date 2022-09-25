import time

from pygame import mixer
import pygame

pygame.init()
mixer.init(channels=5)

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

chan = mixer.find_channel()

sound = mixer.Sound("../../../sounds/test.wav")

sound.play()

sound = mixer.Sound("../../../sounds/sawing_wood.wav")

sound.play()

sound.get_buffer().raw
print(sound.get_raw())

time.sleep(10)

print("end")