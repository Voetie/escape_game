import pygame
import time, sys
class Light(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (128,128)
        self.image = pygame.image.load("images/objects/licht/light0.png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (500,75)
        self.light_switch_audio = pygame.mixer.Sound("sound_files/light_switch.ogg")
        self.light_switch_audio.set_volume(0.1)
        self.light = 0
        self.schilderij = 0

    def update(self, light):
        DEFAULT_IMAGE_SIZE = (160,160)
        self.rect.center = (510,65)
        self.image = pygame.image.load("images/objects/licht/light"+str(light)+".png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
    
    def draw(self,surface):
        surface.blit(self.image,self.rect)

    def audio(self):
        pygame.mixer.Sound.play(self.light_switch_audio)

    def get_light(self):
        return self.light

    def change_light(self, light):
        self.light = light
        self.audio()

    def get_schilderij(self):
        return self.schilderij

    def change_schilderij(self, schilderij):
        self.schilderij = schilderij
        self.update(schilderij)

