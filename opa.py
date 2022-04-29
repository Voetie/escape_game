import pygame
import time, sys

class Opa(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (160,160)
        self.image = pygame.image.load("images/objects_2/opa.gif")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (795,211)

    def draw(self,surface):
        surface.blit(self.image,self.rect)