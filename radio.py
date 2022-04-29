import pygame
import time, sys
class Radio(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (180,180)
        self.image = pygame.image.load("images/objects/radio/radio_on_table1.png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (70,468)
        self.radio_audio = pygame.mixer.Sound("sound_files/radio_audio.ogg")
        self.radio_audio.set_volume(0.095)

    def audio(self):
        pygame.mixer.Sound.play(self.radio_audio)
    
    def update(self, a):
        DEFAULT_IMAGE_SIZE = (180,180)
        self.image = pygame.image.load("images/objects/radio/radio_on_table"+str(a)+".png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)

    def draw(self, surface):  # tekenen op display
        surface.blit(self.image, self.rect)