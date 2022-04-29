import pygame
import time, sys
class Luik(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (128,128)
        self.image = pygame.image.load("images/objects/escape/luik0.png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (850,355)
        self.luik_animation = 0
        self.luik_frame = 0
        self.luik_audio = pygame.mixer.Sound("sound_files/luik_audio.ogg")
        self.luik_audio.set_volume(0.1)
    
    def update(self):
        DEFAULT_IMAGE_SIZE = (128,128)
        if self.luik_frame < 12:
            if self.luik_animation >= (0.13*30):
                self.luik_animation = 0
                self.luik_frame += 1
                self.image = pygame.image.load("images/objects/escape/luik"+ str(self.luik_frame) +".png")
                self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
            self.luik_animation += 1

    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def audio(self):
        pygame.mixer.Sound.play(self.luik_audio)
