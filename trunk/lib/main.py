import sys
import pygame
from pygame.locals import *
import utils
from config import  *
from level import Level
from menu import Menu
from scores import HighScores
from visual import Visual

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def main():
    #Initialize 
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(WINDOW_TITLE)

    images = [utils.load_image(image) for image in INTRO_IMAGES]
    visual = Visual(screen, images, INTRO_TIMES)
    visual.loop()
    
    #Shooter opcion
    opcion = menu
    while opcion is not exit:
        change = opcion(screen).loop()
        if change:
            opcion = change
    opcion()        #Exit

def menu(screen):
    options = [("Play", play), ("Setup", None), ("Help", None), \
               ("High Scores", scores), ("Credits", None), ("Exit",  exit)]
    return Menu(screen, options, WINDOW_TITLE)

def play(screen):
    return Level(screen, menu, 1, 0, 0)

def scores(screen):
    return HighScores(screen,menu)

def exit():
    sys.exit(0)

if __name__ == "__main__":
    main()
