import pygame
from player import Player
from thermometer import Thermometer
from drawer import Drawer
from popups import Popups
from tapijt import Tapijt
from radio import Radio
from library import Library
from safe import Safe
from textblocks import Textblocks
from plant import Plant
from light import Light
from luik import Luik
from verwarming import Verwarming
from speeltijd import Speeltijd
from current_world import CurrentWorld
from speeltijd import Speeltijd

class World:
    def __init__(self, currentworld: CurrentWorld, textblocks: Textblocks):
        #afmeting display
        self.player = Player()
        self.thermometer = Thermometer()
        self.drawer = Drawer()
        self.popups = Popups()
        self.tapijt = Tapijt()
        self.radio = Radio()
        self.library = Library()
        self.safe = Safe()
        self.textblocks = textblocks
        self.plant = Plant()
        self.light = Light()
        self.luik = Luik()
        self.verwarming = Verwarming()
        self.speeltijd = Speeltijd()
        self.worldnow = currentworld

        self.DISPLAYSURF = pygame.display.set_mode((936, 527))
        #afbeelding achtegrond
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (0,0,0)
        self.BLACK = (255,255,255)
        self.speeltijd = Speeltijd()
        self.font = pygame.font.Font('freesansbold.ttf',20)
        self.background = pygame.image.load("images/rooms/kamer1.png")
        self.sdg15 = pygame.image.load("images/objects/popups/popup2.png")
        self.donker = pygame.image.load("images/objects/licht/no_mouse.png")
        self.donker_muis = pygame.image.load("images/objects/licht/mouse.png")
        self.sdg15 = pygame.transform.scale(self.sdg15, (75,75))
        self.DISPLAYSURF = pygame.display.set_mode((936, 527))
        self.pickup_audio = pygame.mixer.Sound("sound_files/pickup_audio.ogg")
        self.pickup_audio.set_volume(0.08)

    def act(self, licht, mousex, mousey, player_movement): #methode act
        self.DISPLAYSURF.blit(self.background, (0, 0))
        self.DISPLAYSURF.blit(self.sdg15, (390,350))
        self.thermometer.update()
        self.thermometer.draw(self.DISPLAYSURF)
        self.drawer.draw(self.DISPLAYSURF)
        self.tapijt.draw(self.DISPLAYSURF)
        self.radio.draw(self.DISPLAYSURF)
        self.library.draw(self.DISPLAYSURF)
        self.safe.draw(self.DISPLAYSURF)
        self.light.draw(self.DISPLAYSURF)
        self.luik.draw(self.DISPLAYSURF)
        self.verwarming.draw(self.DISPLAYSURF)
        if player_movement == 1:
            self.player.update()
        self.player.draw(self.DISPLAYSURF)
        self.plant.draw(self.DISPLAYSURF)
        self.popups.draw(self.DISPLAYSURF)
        if licht == 0:
            self.DISPLAYSURF.blit(self.donker, (0,0))
            self.DISPLAYSURF.blit(self.donker_muis, ((mousex-1920),(mousey-1080)))
        self.textblocks.draw(self.DISPLAYSURF)

    def tekst(self, text, font):
        textsurface = self.font.render(text, True, self.WHITE)
        return textsurface, textsurface.get_rect()

    def gameloss(self, time_message):
        self.textsurf1, self.textrect1 = self.tekst("Je raakte niet op tijd uit de kamer en bent gestorven.", self.font)
        self.textsurf2, self.textrect2 = self.tekst(f"In de tijd dat je speelde zijn er {time_message * 40} bomen omgekapt.", self.font)
        self.textsurf3, self.textrect3 = self.tekst("Wil je het opnieuw proberen? Sluit dit venster af en run de file opnieuw, succes!", self.font)
        self.DISPLAYSURF.fill(self.BLACK)
        self.textrect1.center = (468, 263)
        self.textrect2.center = (468,283)
        self.textrect3.center = (468,360)
        self.DISPLAYSURF.blit(self.textsurf1, self.textrect1)
        self.DISPLAYSURF.blit(self.textsurf2, self.textrect2)
        self.DISPLAYSURF.blit(self.textsurf3, self.textrect3)

    def func_collide(self, sprite1, sprite2) -> bool:
        return sprite1.rect.colliderect(sprite2.rect)

    def mouseclick(self, event, x_min, mousex, x_max, y_min, mousey, y_max) -> bool:
        if (x_min <= mousex <= x_max) and (y_min <= mousey <= y_max):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return True

    def world_1_actions(self, event, mousex, mousey):
        if self.verwarming.get_radiator() == 1:
            self.luik.update()
        if self.thermometer.get_thermo_death() == 1:
            self.gameloss(tijd)
        if self.thermometer.get_thermo_death() != 1:
            tijd = self.speeltijd.playtime_get()
            self.act(self.light.get_light(), mousex, mousey, self.textblocks.get_player_moverment())  # uitvoeren methode act

        if self.light.get_light() == 1:
            if self.func_collide(self.player, self.drawer):
                if self.mouseclick(event, 34, mousex, 125, 61, mousey, 87):
                    if self.plant.get_sleutel() == 1:
                        if self.drawer.get_drawer_frame() == 1:
                            self.drawer.update_drawer_frame(2)
                            self.drawer.audio()
                    elif self.plant.get_sleutel() == 0:
                        self.textblocks.change_textblock(3)

                if self.drawer.get_drawer_frame() == 2:
                    if self.popups.get_popup_nr() == 0:
                        if self.popups.change_popup(event, 60, 90, mousex, mousey, 60, 73, 1):
                            self.drawer.papieraudio()
                    elif self.popups.get_popup_nr() != 0:
                        self.popups.reset_popup(event)
            if self.func_collide(self.player, self.tapijt):
                if self.mouseclick(event, 355, mousex, 400, 256, mousey, 445):
                    if self.tapijt.get_tapijt_frame() != 1:
                        self.tapijt.change_tapijt_frame(1)
                if self.tapijt.get_tapijt_frame() == 1:
                    if self.popups.get_popup_nr() == 0:
                        self.popups.change_popup(event, 390, 406, mousex, mousey, 350, 425, 2)
                    elif self.popups.get_popup_nr() != 0:
                        self.popups.reset_popup(event)
            if self.func_collide(self.player, self.radio):
                if self.mouseclick(event, 47, mousex, 95, 422, mousey, 450):
                    if self.library.get_batterij() == 1:
                        self.radio.audio()
                    else:
                        self.textblocks.change_textblock(1)
            if self.func_collide(self.player, self.library):
                if self.library.get_batterij() == 1:
                    if self.popups.get_popup_nr() == 0:
                        self.popups.change_popup(event, 776, 923, mousex, mousey, 0, 195, 3)
                    elif self.popups.get_popup_nr() != 0:
                        self.popups.reset_popup(event)

                if self.library.get_batterij() == 0:
                    if self.popups.get_popup_nr() == 0:
                        self.popups.change_popup(event, 776, 923, mousex, mousey, 0, 195, 5)

                    elif self.popups.get_popup_nr() == 5:
                        if self.popups.change_popup(event, 130, 200, mousex, mousey, 435, 463, 3):
                                pygame.mixer.Sound.play(self.pickup_audio)
                                self.library.update_batterij(1)
                        elif self.popups.get_popup_nr() != 0:
                            self.popups.reset_popup(event)
            if self.func_collide(self.player, self.safe):
                if self.safe.get_kluis_code_situation() == 1:
                    if self.mouseclick(event, 461, mousex, 474, 280, mousey, 300):
                        if self.safe.get_kluis_tang() == 2:
                            self.safe.update_kluis_tang(3)
                            self.safe.update(3)
                            pygame.mixer.Sound.play(self.pickup_audio)
                    if self.mouseclick(event, 440, mousex, 484, 268, mousey, 307):
                        if self.safe.get_kluis_tang() == 0:
                            self.safe.update_kluis_tang(2)
                            self.safe.update(2)
                if self.safe.get_kluis_code_situation() == 0:
                    if self.popups.get_popup_nr() == 0:
                        self.popups.change_popup(event, 438, 483, mousex, mousey, 268, 308, 4)
                    elif self.popups.get_popup_nr() == 4:
                        if self.safe.kluis_code(event):
                            self.popups.update(0)
            if self.func_collide(self.player, self.plant):
                if self.plant.get_sleutel() == 1:
                    if self.popups.get_popup_nr() == 0:
                        self.popups.change_popup(event, 870, 910, mousex, mousey, 432, 453, 7)
                    elif self.popups.get_popup_nr() == 7:
                        self.popups.reset_popup(event)

                elif self.plant.get_sleutel() == 0:
                    if self.popups.get_popup_nr() == 0:
                        self.popups.change_popup(event, 870, 910, mousex, mousey, 432, 453, 6)

                    elif self.popups.get_popup_nr() == 6:
                        if self.popups.change_popup(event, 0, 32, mousex, mousey, 287, 345, 7):
                            pygame.mixer.Sound.play(self.pickup_audio)
                            self.plant.update_sleutel(1)
                        elif popups.get_popup_nr() != 0:
                            self.popups.reset_popup(event)
            if self.verwarming.get_radiator() == 0:
                if self.func_collide(self.player, self.verwarming):
                    if self.mouseclick(event, 258, mousex, 297, 156, mousey, 188):
                        if self.safe.get_kluis_tang() == 3:
                            self.verwarming.update_radiator(1)
                            self.textblocks.change_textblock(6)
                            self.verwarming.audio()
                            self.verwarming.update(1)
                            self.luik.audio()
                        else:
                            self.textblocks.change_textblock(5)
            if self.verwarming.get_radiator() == 1:
                if self.func_collide(self.player, self.luik):
                    self.textblocks.show_tip(7)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.worldnow.change_world(2)
        if self.light.get_light() == 0:
            if self.func_collide(self.player, self.light):
                if self.light.get_schilderij() == 1:
                    if self.mouseclick(event, 473, mousex, 484, 98, mousey, 117):
                        self.light.change_schilderij(2)
                        self.light.change_light(1)
                if self.light.get_schilderij() == 0:
                    if self.mouseclick(event, 46, mousex, 538, 34, mousey, 106):
                        self.light.change_schilderij(1)
