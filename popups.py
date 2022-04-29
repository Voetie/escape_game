import pygame
import time, sys
class Popups(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        DEFAULT_IMAGE_SIZE = (600,600)
        self.popup_nr = 0
        self.image = pygame.image.load("images/objects/popups/popup"+ str(self.popup_nr) +".png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (468,263)


    def update(self,b):
        self.popup_nr = b
        self.image = pygame.image.load("images/objects/popups/popup"+ str(self.popup_nr) +".png")
        height = self.image.get_height() 
        width = self.image.get_width()
        A = 527 / height
        B = 936 / width
        C = min(A,B)
        DEFAULT_IMAGE_SIZE = (width*C,height*C)
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (468,263)

    def draw(self, surface):  # tekenen op display
        surface.blit(self.image, self.rect)

    def get_popup_nr(self):
        return self.popup_nr

    def change_popup(self,event, x_min, x_max, mousex, mousey, y_min, y_max, situatie_popup) ->bool:
            if (x_min <= mousex <= x_max) and (y_min <= mousey <= y_max):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.popup_nr = situatie_popup
                        self.update(situatie_popup)
                        pygame.display.update()
                        return True

    def reset_popup(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.popup_nr = 0
                self.update(self.popup_nr)
                pygame.display.update()
