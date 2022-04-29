import pygame
import time, sys

class Plant(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (92,92)
        self.image = pygame.image.load("images/objects/plant/plant.png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (890,470)
        self.sleutel = 0

    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def get_sleutel(self):
        return self.sleutel

    def update_sleutel(self,sleutel):
        self.sleutel = sleutel