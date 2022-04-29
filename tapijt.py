import pygame
import time, sys
class Tapijt(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (190,190)
        self.image = pygame.image.load("images/objects/tapijt.png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (450,350)
        self.tapijt_audio = pygame.mixer.Sound("sound_files/tapijt_audio.ogg")
        self.tapijt_audio.set_volume(0.1)
        self.tapijt_frame = 0

    def update(self,c):
        self.rect.move_ip(50*c, 0)

    def draw(self, surface):  # tekenen op display
        surface.blit(self.image, self.rect)

    def audio(self):
        pygame.mixer.Sound.play(self.tapijt_audio)

    def get_tapijt_frame(self):
        return self.tapijt_frame

    def change_tapijt_frame(self, frame):
        self.tapijt_frame = frame
        self.update(self.tapijt_frame)
        self.audio()