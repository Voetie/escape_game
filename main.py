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


# functies
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
P = Player()
thermo = Thermometer()
drawer = Drawer()
popups = Popups()
tapijt = Tapijt()
radio = Radio()
library = Library()
safe = Safe()
textblocks = Textblocks()
plant = Plant()
light = Light()
luik = Luik()
verwarming = Verwarming()
world = World(
    P,
    thermo,
    drawer,
    popups,
    tapijt,
    radio,
    library,
    safe,
    textblocks,
    plant,
    light,
    luik,
    verwarming,
)

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
    print(mousex, mousey)

    if worldnow.get_current_world() == 1:
        if verwarming.get_radiator() == 1:
            luik.update()
        if thermo.get_thermo_death() == 1:
            world.gameloss(tijd)
        if thermo.get_thermo_death() != 1:
            tijd = speeltijd.playtime_get()
            world.act(
                light.get_light(), mousex, mousey, textblocks.get_player_moverment()
            )  # uitvoeren methode act
        textblocks.intro_text()

        for event in pygame.event.get():
            if event.type == pygame.constants.QUIT:
                pygame.quit()
                sys.exit()
            if light.get_light() == 1:
                if func_collide(P, drawer):
                    if mouseclick(event, 34, mousex, 125, 61, mousey, 87):
                        if plant.get_sleutel() == 1:
                            if drawer.get_drawer_frame() == 1:
                                drawer.update_drawer_frame(2)
                                drawer.audio()
                        elif plant.get_sleutel() == 0:
                            textblocks.change_textblock(3)

                    if drawer.get_drawer_frame() == 2:
                        if popups.get_popup_nr() == 0:
                            if popups.change_popup(
                                event, 60, 90, mousex, mousey, 60, 73, 1
                            ):
                                drawer.papieraudio()
                        elif popups.get_popup_nr() != 0:
                            popups.reset_popup(event)
                if func_collide(P, tapijt):
                    if mouseclick(event, 355, mousex, 400, 256, mousey, 445):
                        if tapijt.get_tapijt_frame() != 1:
                            tapijt.change_tapijt_frame(1)
                    if tapijt.get_tapijt_frame() == 1:
                        if popups.get_popup_nr() == 0:
                            popups.change_popup(
                                event, 390, 406, mousex, mousey, 350, 425, 2
                            )
                        elif popups.get_popup_nr() != 0:
                            popups.reset_popup(event)
                if func_collide(P, radio):
                    if mouseclick(event, 47, mousex, 95, 422, mousey, 450):
                        if library.get_batterij() == 1:
                            radio.audio()
                        else:
                            textblocks.change_textblock(1)
                if func_collide(P, library):
                    if library.get_batterij() == 1:
                        if popups.get_popup_nr() == 0:
                            popups.change_popup(
                                event, 776, 923, mousex, mousey, 0, 195, 3
                            )
                        elif popups.get_popup_nr() != 0:
                            popups.reset_popup(event)

                    if library.get_batterij() == 0:
                        if popups.get_popup_nr() == 0:
                            popups.change_popup(
                                event, 776, 923, mousex, mousey, 0, 195, 5
                            )

                        elif popups.get_popup_nr() == 5:
                            if popups.change_popup(
                                event, 130, 200, mousex, mousey, 435, 463, 3
                            ):
                                pygame.mixer.Sound.play(pickup_audio)
                                library.update_batterij(1)
                            elif popups.get_popup_nr() != 0:
                                popups.reset_popup(event)
                if func_collide(P, safe):
                    if safe.get_kluis_code_situation() == 1:
                        if mouseclick(event, 461, mousex, 474, 280, mousey, 300):
                            if safe.get_kluis_tang() == 2:
                                safe.update_kluis_tang(3)
                                safe.update(3)
                                pygame.mixer.Sound.play(pickup_audio)
                        if mouseclick(event, 440, mousex, 484, 268, mousey, 307):
                            if safe.get_kluis_tang() == 0:
                                safe.update_kluis_tang(2)
                                safe.update(2)
                    if safe.get_kluis_code_situation() == 0:
                        if popups.get_popup_nr() == 0:
                            popups.change_popup(
                                event, 438, 483, mousex, mousey, 268, 308, 4
                            )
                        elif popups.get_popup_nr() == 4:
                            if safe.kluis_code(event):
                                popups.update(0)
                if func_collide(P, plant):
                    if plant.get_sleutel() == 1:
                        if popups.get_popup_nr() == 0:
                            popups.change_popup(
                                event, 870, 910, mousex, mousey, 432, 453, 7
                            )
                        elif popups.get_popup_nr() == 7:
                            popups.reset_popup(event)

                    elif plant.get_sleutel() == 0:
                        if popups.get_popup_nr() == 0:
                            popups.change_popup(
                                event, 870, 910, mousex, mousey, 432, 453, 6
                            )

                        elif popups.get_popup_nr() == 6:
                            if popups.change_popup(
                                event, 0, 32, mousex, mousey, 287, 345, 7
                            ):
                                pygame.mixer.Sound.play(pickup_audio)
                                plant.update_sleutel(1)
                            elif popups.get_popup_nr() != 0:
                                popups.reset_popup(event)
                if verwarming.get_radiator() == 0:
                    if func_collide(P, verwarming):
                        if mouseclick(event, 258, mousex, 297, 156, mousey, 188):
                            if safe.get_kluis_tang() == 3:
                                verwarming.update_radiator(1)
                                textblocks.change_textblock(6)
                                verwarming.audio()
                                verwarming.update(1)
                                luik.audio()
                            else:
                                textblocks.change_textblock(5)
                if verwarming.get_radiator() == 1:
                    if func_collide(P, luik):
                        textblocks.show_tip(7)
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                worldnow.change_world(2)
            if light.get_light() == 0:
                if func_collide(P, light):
                    if light.get_schilderij() == 1:
                        if mouseclick(event, 473, mousex, 484, 98, mousey, 117):
                            light.change_schilderij(2)
                            light.change_light(1)
                    if light.get_schilderij() == 0:
                        if mouseclick(event, 46, mousex, 538, 34, mousey, 106):
                            light.change_schilderij(1)

    elif worldnow.get_current_world() == 2:
        world2.act()
        pygame.display.update()
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
                                pygame.display.update()

                        elif situatie_popup == 1:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    situatie_popup = 0
                                    popups.update(situatie_popup)
                                    pygame.display.update()

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
