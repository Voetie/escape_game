import pygame
import time, sys
class Textblocks(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.DEFAULT_IMAGE_SIZE = (666,375)
        self.image = pygame.image.load("images/objects/text/textblock2.png")
        self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (468,339)
        self.tekst = 2
        self.tekst_teller = 0
        self.intro = 0
        self.dialogue = pygame.mixer.Sound("sound_files/dialogue.ogg")
        self.dialogue.set_volume(0.08)
        self.player_movement = 0
        pygame.mixer.Sound.play(self.dialogue)

    def update(self,tekst):
        self.image = pygame.image.load("images/objects/text/textblock"+ str(tekst) +".png")
        self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
        pygame.display.update()

    def draw(self, surface):  # tekenen op display
        surface.blit(self.image, self.rect)

    def get_textblock(self):
        return self.tekst

    def intro_text(self):
        
        if self.intro == 0:
            if self.tekst == 2:
                if self.tekst_teller >= (30 * 7):
                    self.tekst = 4
                    self.update(self.tekst)
                    pygame.mixer.Sound.play(self.dialogue)
                    pygame.display.update()
                    self.tekst_teller = 0
                self.tekst_teller += 1
            if self.tekst == 4:
                if self.tekst_teller >= (30 * 6):
                    self.intro = 1
                    self.player_movement = 1
                    self.tekst = 0
                    self.update(self.tekst)
                    self.tekst_teller = 0
                self.tekst_teller += 1

    def get_intro(self):
        return self.intro
    
    def get_player_moverment(self):
        return self.player_movement

    def reset_text(self):
        if self.tekst != 0:
            if self.tekst_teller >= (30 * 5):
                self.tekst = 0
                self.update(self.tekst)
                self.tekst_teller = 0
            self.tekst_teller += 1

    def change_textblock(self, text):
        self.tekst = text
        pygame.mixer.Sound.play(self.dialogue)
        self.update(self.tekst)
    
    def show_tip(self,text):
        self.tekst = text
        self.update(self.tekst)
