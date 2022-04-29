import pygame
import time, sys

class Kraan(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (600,400)
        self.image = pygame.image.load("images/objects_2/kraan.png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (200,400)

    def draw(self,surface):
        surface.blit(self.image,self.rect)