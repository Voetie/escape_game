import pygame
import time, sys

class Plant2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (120, 120)
        self.image = pygame.image.load("images/objects/plant/plant.png")
        # deze afbeelding kan vervangen worden door een andere soort plant
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (845, 400)  

    def draw(self, surface):
        surface.blit(self.image, self.rect)
