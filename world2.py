import pygame
from player2 import Player2
from mat import Mat
from plant2 import Plant2
from water import Water
from bureau import Bureau
from kraan import Kraan
from opa import Opa
from popups import Popups
from kist import Kist
from poster import Poster
from popups2 import Popups2



class World2:
    def __init__(self, player2: Player2, mat: Mat, plant2: Plant2, water: Water, bureau: Bureau, kraan: Kraan, opa: Opa, popups: Popups, kist: Kist, poster: Poster):
        self.DISPLAYSURF = pygame.display.set_mode((936,527)) #VERVANG DEZE GETALLEN DOOR DE AFMETINGEN VAN JE ACHTERGRONDFOTO
        self.background = pygame.image.load("images/rooms/kamer1.png") #PAS DIT NOG AAN!!! DIT WAS GEWOON VOOR MIJ OM TE TESTEN ALS HET WERKTE
        self.DISPLAYSURF = pygame.display.set_mode((936,527)) #zelfde achtergrond wordt behouden dus is niet nodig om te veranderen
        self.player2 = player2
        self.mat = mat
        self.plant2 = plant2
        self.water = water
        self.bureau = bureau
        self.kraan = kraan
        self.opa = opa
        self.popups = popups
        self.kist = kist
        self.poster = poster
        
        
    
    def act(self): #methode act
        self.DISPLAYSURF.blit(self.background, (0, 0))
        self.mat.draw(self.DISPLAYSURF)
        self.plant2.draw(self.DISPLAYSURF)
        self.poster.draw(self.DISPLAYSURF)
        self.kist.draw(self.DISPLAYSURF)
        self.water.update()
        self.water.draw(self.DISPLAYSURF)
        self.bureau.draw(self.DISPLAYSURF)
        self.kraan.draw(self.DISPLAYSURF)
        self.opa.draw(self.DISPLAYSURF)
        self.popups.draw(self.DISPLAYSURF)
        self.player2.update()
        self.player2.draw(self.DISPLAYSURF)
    
