from config import *
import utils
import pygame
pygame.init()

SOUNDS = {}
SOUNDS['eat'] = utils.load_sound(BLOOP)

def play_bloop():
    SOUNDS['eat'].play()
