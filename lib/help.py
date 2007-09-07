import pygame
import random
from twist import twist
import utils
from config import *
import music
import sys
from pygame.locals import *


class Help(object):

    def __init__(self,screen,father):
        self.screen = screen
        self.father = father
        self.done = False
        self.font0 = pygame.font.Font(FONT1, 65)
        self.background = utils.load_image(MENUBGIMAGE)
        
    def loop(self):

        while not self.done:

            #self.clock.tick(10)

            self.screen.blit(self.background, (0,0))    

            for event in pygame.event.get():
                self.control(event)

     
            texto = self.font0.render("PROBANDO EL HELP", True,(200,60,50)) #aca podria llamar a un archivo con todo el texto
            self.screen.blit(texto, (20,20))
            pygame.display.flip()
            
        return self.father
            

    def control(self, event):
        if event.type == KEYDOWN:
            if event.key in (K_SPACE, K_RETURN, K_KP_ENTER, K_DOWN):
                self.done = True


