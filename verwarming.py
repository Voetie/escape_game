import pygame
import time, sys
class Verwarming(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.DEFAULT_IMAGE_SIZE = (200,200)
        self.image = pygame.image.load("images/objects/radiator/radiator0.png")
        self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (240,155)
        self.radiator_shutoff = pygame.mixer.Sound("sound_files/radiator_shutoff.ogg")
        self.radiator_shutoff.set_volume(0.1)
        self.radiator = 0

    def update(self,radiator):
        self.image = pygame.image.load("images/objects/radiator/radiator"+ str(radiator) +".png")
        self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)

    def draw(self, surface):  # tekenen op display
        surface.blit(self.image, self.rect)

    def audio(self):
        pygame.mixer.Sound.play(self.radiator_shutoff)

    def get_radiator(self):
        return self.radiator

    def update_radiator(self, radiator):
        self.radiator = radiator