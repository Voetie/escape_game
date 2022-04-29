import pygame
import time, sys
class Water(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (140,140)
        self.getal = 1
        self.image = pygame.image.load("images/objects_2/raam_water/raam_1.png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (500,75)
        self.a = 0
    
    def update(self):
        DEFAULT_IMAGE_SIZE = (140,140)
        if self.a >= (35*30):
            self.getal += 1
            self.image = pygame.image.load("images/objects_2/raam_water/raam_"+ str(self.getal) +".png")
            self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
            self.a = 0
        if self.getal > 15:
            pygame.quit()
            sys.exit()
        self.a += 1

    def draw(self, surface):  # tekenen op display
        surface.blit(self.image, self.rect)