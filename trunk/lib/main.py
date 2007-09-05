import pygame
from pygame.locals import *
import utils
from config import  *
from level import Level

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def main():
    #Initialize 
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(WINDOW_TITLE)

    background = utils.create_surface((width, height), (0,0,0))
    screen.blit(background, (0, 0))

    Level(screen).loop()


if __name__ == "__main__":
    main()
