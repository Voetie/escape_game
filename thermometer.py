import pygame
import time, sys
class Thermometer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.DEFAULT_IMAGE_SIZE = (164,164)
        self.getal = 1
        self.image = pygame.image.load("images/objects/thermometer/thermo1.png")
        self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (750,70)
        self.a = 0
        self.dead = 0
    
    def update(self):
        if self.a > (42*30):
            self.getal += 1
            try:
                self.image = pygame.image.load("images/objects/thermometer/thermo"+ str(self.getal) +".png")
                self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
            except FileNotFoundError:
                self.thermo_death()
            self.a = 0
        self.a += 1

    def thermo_death(self):
        self.dead = 1

    def get_thermo_death(self):
        return self.dead

    def draw(self, surface):  # tekenen op display
        surface.blit(self.image, self.rect)