import pygame
import time, sys
class Library(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (150,200)
        self.image = pygame.image.load("images/objects/bookshelf/bookshelf.png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (850,100)
        self.batterij = 0

    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def get_batterij(self):
        return self.batterij

    def update_batterij(self,batterij):
        self.batterij = batterij




