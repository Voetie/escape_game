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

class World:
    def __init__(self, player: Player, thermometer: Thermometer, drawer: Drawer, popups: Popups, tapijt: Tapijt, radio : Radio, library: Library, safe: Safe, textblocks: Textblocks, plant:Plant, light: Light, luik:Luik, verwarming:Verwarming):
        #afmeting display
        self.DISPLAYSURF = pygame.display.set_mode((936, 527))
        #afbeelding achtegrond
        kamer = "kamer1"
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
        self.player = player
        self.thermometer = thermometer
        self.drawer = drawer
        self.popups = popups
        self.tapijt = tapijt
        self.radio = radio
        self.library = library
        self.safe = safe
        self.textblocks = textblocks
        self.plant = plant
        self.light = light
        self.luik = luik
        self.verwarming = verwarming

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