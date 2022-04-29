import pygame
import random
import time, sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        # afbeelding en positie greeps
        super().__init__()
        DEFAULT_IMAGE_SIZE = (128, 128)
        movement = {"up" : ["up1","up2","up3","up4"], "down" : ["down1","down2","down3","down4"
        ], "left" : ["left1","left2","left3","left4"], "right" : ["right1","right2","right3","right4"]}
        tile = "down1"
        self.image = pygame.image.load("images/character/tiles/"+ tile +".png")
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.x = 330
        self.y = 170
        self.rect.center = (330,170)
        self.teller = 0
        self.animation_time = 0


    def update(self):
        footstep_audio = pygame.mixer.Sound("sound_files/footstep.ogg")
        footstep_audio.set_volume(0.03)
        DEFAULT_IMAGE_SIZE = (128, 128)
        movement = {"up" : ["up1","up2","up3","up4"], "down" : ["down1","down2","down3","down4"
        ], "left" : ["left1","left2","left3","left4"], "right" : ["right1","right2","right3","right4"]}
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if not (keys[pygame.K_DOWN] or keys[pygame.K_s] or keys[pygame.K_UP] or keys[pygame.K_z] or keys[pygame.K_LEFT] or keys[pygame.K_q]):
                if (self.x < 918) and not ((200 <= self.y <= 342) and (360 <= self.x <= 531)) and not (( 450 <= self.y <= 600) and (833 <= self.x <= 1000)):
                    if self.animation_time >= (0.13*30):
                        self.animation_time = 0
                        self.rect.move_ip(12, 0)
                        self.x += 12
                        tile = movement["right"][self.teller%4]
                        self.image = pygame.image.load("images/character/tiles/"+ tile +".png")
                        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
                        pygame.mixer.Sound.play(footstep_audio)
                        self.teller +=1
                    self.animation_time += 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if not (keys[pygame.K_UP] or keys[pygame.K_z] or keys[pygame.K_LEFT] or keys[pygame.K_q] or keys[pygame.K_RIGHT] or keys[pygame.K_d]):
                if (self.y < 480) and not ((0 <= self.x <= 170) and (self.y > 345)) and not ((187 <= self.y <= 355) and (373 <= self.x <= 531)) and not ((420 <= self.y <= 600 ) and (833 <= self.x <= 1000)):
                    if self.animation_time >= (0.13*30):
                        self.animation_time = 0
                        self.rect.move_ip(0, 12)
                        self.y += 12
                        tile = movement["down"][self.teller%4]
                        self.image = pygame.image.load("images/character/tiles/"+ tile +".png")
                        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
                        pygame.mixer.Sound.play(footstep_audio)
                        self.teller +=1
                    self.animation_time += 1
        if keys[pygame.K_UP] or keys[pygame.K_z]:
            if not (keys[pygame.K_DOWN] or keys[pygame.K_s] or keys[pygame.K_LEFT] or keys[pygame.K_q] or keys[pygame.K_RIGHT] or keys[pygame.K_d]):
                if (self.y > 150) and not ((200 <= self.y <= 355) and (373 <= self.x <= 531)):
                    if self.animation_time >= (0.13*30):
                        self.animation_time = 0
                        self.rect.move_ip(0, -12)
                        self.y -= 12
                        tile = movement["up"][self.teller%4]
                        self.image = pygame.image.load("images/character/tiles/"+ tile +".png")
                        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
                        pygame.mixer.Sound.play(footstep_audio)
                        self.teller +=1
                    self.animation_time += 1
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            if not (keys[pygame.K_DOWN] or keys[pygame.K_s] or keys[pygame.K_UP] or keys[pygame.K_z] or keys[pygame.K_RIGHT] or keys[pygame.K_d]):
                if (self.x > 26) and not ((360 <= self.y <= 600) and (self.x < 180)) and not ((200 <= self.y <= 342) and (373 <= self.x <= 544)):
                    if self.animation_time >= (0.13*30):
                        self.animation_time = 0
                        self.rect.move_ip(-12, 0)
                        self.x -=12
                        tile = movement["left"][self.teller%4]
                        self.image = pygame.image.load("images/character/tiles/"+ tile +".png")
                        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
                        pygame.mixer.Sound.play(footstep_audio)
                        self.teller +=1
                    self.animation_time += 1
        
    def draw(self, surface):  # tekenen op display
        surface.blit(self.image, self.rect)