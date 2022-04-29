import pygame
import time, sys
class Drawer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (190,190)
        self.image = pygame.image.load("images/objects/drawer/drawer1.png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (80,100)
        self.papier_audio = pygame.mixer.Sound("sound_files/paper_pickup.ogg")
        self.papier_audio.set_volume(0.08)
        self.drawer_audio = pygame.mixer.Sound("sound_files/open_drawer.ogg")
        self.drawer_audio.set_volume(0.08)
        self.drawer_frame = 1

    def update(self,drawer):
        DEFAULT_IMAGE_SIZE = (190,190)
        self.image = pygame.image.load("images/objects/drawer/drawer"+ str(drawer) +".png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)

    def draw(self, surface):  # tekenen op display
        surface.blit(self.image, self.rect)

    def audio(self):
        pygame.mixer.Sound.play(self.drawer_audio)

    def papieraudio(self):
        pygame.mixer.Sound.play(self.papier_audio)

    def get_drawer_frame(self):
        return self.drawer_frame

    def update_drawer_frame(self, frame):
        self.drawer_frame = frame
        self.update(self.drawer_frame)
