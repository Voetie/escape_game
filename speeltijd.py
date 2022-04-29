import pygame
import time, sys

class Speeltijd(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.klok = 0
        self.time = 0
        self.clock_tick = pygame.mixer.Sound("sound_files/clock_tick.ogg")
        self.clock_tick.set_volume(0.01)
        speeltijd = 0

    def playtime(self):
        if self.klok >= 30:
            self.klok = 0
            self.time += 1
            pygame.mixer.Sound.play(self.clock_tick)
        self.klok += 1

    def playtime_get(self):
        return self.time
