import pygame
import time, sys


class Mat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (200, 200)
        self.image = pygame.image.load("images/objects_2/mat.png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (842, 440)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
