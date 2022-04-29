import pygame
import time, sys


class Poster(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (100, 100)
        self.image = pygame.image.load("images/objects_2/poster.gif")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (800, 75)

    # coordinaten: x:40-120   (handig voor popup)
    #              y:400-490
    def draw(self, surface):
        surface.blit(self.image, self.rect)
