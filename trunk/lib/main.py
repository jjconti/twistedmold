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

    background = utils.create_surface((width, height), (0,0,0))
    screen.blit(background, (0, 0))

  	#Shooter opcion
    opcion = menu
    while opcion is not exit:
        change = opcion(screen).loop()
        if change:
            opcion = change
    opcion()        #Exit

def menu(screen):
    options = [("Play", play), ("Story", None), ("Setup", None), \
               ("Help", None), ("Exit",  exit)]
    return Menu(screen, options, WINDOW_TITLE)

def play(screen):
    return Level(screen)

def exit():
    sys.exit(0)

if __name__ == "__main__":
    main()
