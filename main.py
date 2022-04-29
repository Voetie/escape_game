import pygame
from pygame.locals import *
from pygame import mixer
import time, sys
from speeltijd import Speeltijd
from current_world import CurrentWorld

# imports voor kamer 1
from world import World
from player import Player
from thermometer import Thermometer
from drawer import Drawer
from popups import Popups
from radio import Radio
from library import Library
from safe import Safe
from textblocks import Textblocks
from plant import Plant
from light import Light
from luik import Luik
from verwarming import Verwarming
from tapijt import Tapijt
# imports voor kamer 2
from world2 import World2
from player2 import Player2
from mat import Mat
from plant2 import Plant2
from water import Water
from kraan import Kraan
from bureau import Bureau
from opa import Opa
from popups2 import Popups2

# from popups2 import Popups2
from kist import Kist
from poster import Poster


#functies
def mouseclick(event, x_min, mousex, x_max, y_min, mousey, y_max) -> bool:
    if (x_min <= mousex <= x_max) and (y_min <= mousey <= y_max):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return True

def func_collide(sprite1, sprite2) -> bool:
    return sprite1.rect.colliderect(sprite2.rect)

pygame.init()
pygame.display.set_caption("Escapegame Team 10")
FPS = pygame.time.Clock()
keys = pygame.key.get_pressed()


# sound effects
mixer.init()
background_music = pygame.mixer.Sound("sound_files/background.ogg")
background_music.set_volume(0.02)
pygame.mixer.Sound.play(background_music)
pickup_audio = pygame.mixer.Sound("sound_files/pickup_audio.ogg")
pickup_audio.set_volume(0.08)

# variabelen
raam = 0
mat = 0
plant2 = 0
# situatie2_popup = 0
kist = 0
situatie_kist = 0
worldnow = CurrentWorld()

# sprites invoegen in main voor kamer 1
textblocks = Textblocks()
world = World(worldnow, textblocks)

# sprites invoegen in main voor kamer 2
speeltijd = Speeltijd()
P2 = Player2()
mat = Mat()
plant2 = Plant2()
water = Water()
poster = Poster()
bureau = Bureau()
kraan = Kraan()
opa = Opa()
kist = Kist()
popups = Popups()
world2 = World2(
    P2, mat, plant2, water, bureau, kraan, opa, popups, kist, poster
)  # was popups2

while True:
    FPS.tick(30)
    speeltijd.playtime()
    pygame.display.update() 
    mousex, mousey = pygame.mouse.get_pos()
    if textblocks.get_intro() == 1:
        textblocks.reset_text()
    textblocks.intro_text()
    print(mousex, mousey)

    for event in pygame.event.get():
        if event.type == pygame.constants.QUIT:
            pygame.quit()
            sys.exit()
        
    if worldnow.get_current_world() == 1:
        world.world_1_actions(event, mousex, mousey)

    elif worldnow.get_current_world() == 2:
        world2.act()
        for event in pygame.event.get():
            if event.type == pygame.constants.QUIT:
                pygame.quit()
                sys.exit()

            if func_collide(P2, opa):
                if situatie_popup == 0:
                    if (715 <= mousex <= 875) and (131 <= mousey <= 291):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                situatie_popup = 8
                                popups.update(situatie_popup)

                        elif situatie_popup == 1:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    situatie_popup = 0
                                    popups.update(situatie_popup)

            if func_collide(P2, kist):
                if situatie_popup == 0:
                    if (40 <= mousex <= 120) and (400 <= mousey <= 490):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                situatie_popup = 1
                                popups.update(situatie_popup)
                                pygame.display.update()

                        elif situatie_popup == 1:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    situatie_popup = 0
                                    popups.update(situatie_popup)
                                    pygame.display.update()