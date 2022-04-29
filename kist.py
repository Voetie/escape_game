import pygame
import time, sys


class Kist(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (80, 80)
        self.image = pygame.image.load("images/objects_2/chest.gedraaid.png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (80, 446)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
