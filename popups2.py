import pygame
import time, sys
class Popups2(pygame.sprite.Sprite):
    def __init__(self, b):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (600,600)
        self.image = pygame.image.load("images/objects_2/popups2/popup"+ str(b) +".png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (468,263)

    def update(self,b):
        self.image = pygame.image.load("images/objects_2/popups2/popup"+ str(b) +".png")
        height = self.image.get_height() 
        width = self.image.get_width()
        A = 527 / height
        B = 936 / width
        C = min(A,B)
        DEFAULT_IMAGE_SIZE = (width*C,height*C)
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (468,263)

    def draw(self, surface): 
        surface.blit(self.image, self.rect)