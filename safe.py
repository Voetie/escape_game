import pygame
import time, sys
from popups import Popups
class Safe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (120,120)
        self.image = pygame.image.load("images/objects/safe/1.png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (450,310)
        self.wrong_code = pygame.mixer.Sound("sound_files/wrong_code.ogg")
        self.wrong_code.set_volume(0.08)
        self.correct_code = pygame.mixer.Sound("sound_files/correct_code.ogg")
        self.correct_code.set_volume(0.08)
        self.button_push_audio = pygame.mixer.Sound("sound_files/button_push_audio.ogg")
        self.button_push_audio.set_volume(0.1)
        self.kluis_situation = 0
        self.counter_kluis = 0
        self.combinatie_kluis = []
        self.popups = Popups()
        self.kluis_tang = 0

    def update(self,a):
        DEFAULT_IMAGE_SIZE = (120,120)
        self.image = pygame.image.load("images/objects/safe/" + str(a) + ".png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)

    def draw(self, surface):  # tekenen op display
        surface.blit(self.image, self.rect)
    
    # Probleem afspelen geluid
    def audio(self,nr):
        if nr==0:
            pygame.mixer.Sound.play(self.button_push_audio)
        elif nr==1:
            pygame.mixer.Sound.play(self.correct_code)
        elif nr == 2:
            pygame.mixer.Sound.play(self.wrong_code)

    def get_kluis_code_situation(self):
        return self.kluis_situation

    def get_kluis_tang(self):
        return self.kluis_tang

    def update_kluis_tang(self, tang):
        self.kluis_tang = tang

    def kluis_code(self, event):
            if self.counter_kluis < 4:
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.name(event.key)
                    if key in "0123456789":
                        kluis_key = int(key)
                        self.combinatie_kluis.append(kluis_key)
                        self.counter_kluis += 1
                        self.audio(0)
                    elif str(key[1]) in "0123456789":
                        kluis_key = int(key[1])
                        self.combinatie_kluis.append(kluis_key)
                        self.counter_kluis += 1
                        self.audio(0)
            elif self.counter_kluis == 4:
                if self.combinatie_kluis == [2, 0, 6, 7]:
                    self.kluis_situation = 1
                    self.audio(1)
                    return True
                else:
                    self.combinatie_kluis = []
                    self.counter_kluis = 0
                    self.audio(2)
                    return True