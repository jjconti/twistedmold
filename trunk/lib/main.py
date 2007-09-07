import sys
import pygame
from pygame.locals import *
import utils
from config import  *
from level import Level
from menu import Menu
from scores import HighScores
from visual import Visual

from help import Help

from credits import Credits


if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def main():
    #Initialize 
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    icon = utils.load_image(ICON)
    pygame.display.set_icon(icon)

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
    options = [("Play", play), ("Story", None), ("Help", help), \
               ("High Scores", scores), ("Credits", credits), ("Exit",  exit)]
    return Menu(screen, options, WINDOW_TITLE)

def play(screen):
    return Level(screen, menu, 1, 0, 0)

def scores(screen):
    return HighScores(screen,menu)


def help(screen):
    return Help(screen,menu)


def credits(screen):
    return Credits(screen,menu)


def exit():
    sys.exit(0)

if __name__ == "__main__":
    main()
