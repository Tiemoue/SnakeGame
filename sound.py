import pygame
from pygame import mixer

mixer.init()


def music(track):
    pygame.mixer.music.load(track)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1, -1)


def sound(track, volume):
    effect = pygame.mixer.Sound(track)
    effect.set_volume(volume)
    effect.play()


theme = "assets/wacky.wav"
endgame = "assets/defeat.wav"
eat = "assets/ring.wav"
