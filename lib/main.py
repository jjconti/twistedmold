import sys
import pygame
from pygame.locals import *
import utils
from config import  *
from level import Level
from menu import Menu

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def main():
    #Initialize 
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(WINDOW_TITLE)

  	#Shooter opcion
    opcion = menu
    while opcion is not exit:
        change = opcion(screen).loop()
        if change:
            opcion = change
    opcion()        #Exit

def menu(screen):
    options = [("Play", play), ("Story", None), ("Setup", None), \
               ("Help", None), ("Credits", None), ("Exit",  exit)]
    return Menu(screen, options, WINDOW_TITLE)

def play(screen):
    return Level(screen, menu, 1, 0)

def exit():
    sys.exit(0)

if __name__ == "__main__":
    main()
