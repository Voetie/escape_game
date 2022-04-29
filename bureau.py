import pygame
import time, sys


class Bureau(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (220, 220)
        self.image = pygame.image.load("images/objects_2/bureau.png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (180, 60)  

    def draw(self, surface):
        surface.blit(self.image, self.rect)