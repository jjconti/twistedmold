import pygame
import random
from sprites import Bottle
from twist import twist
import utils
from config import *
import music

class BottleManager(object):

    def __init__(self):
        self.bottles = pygame.sprite.Group()
        self.bottle_density = 444

    def draw(self, screen):
        self.bottles.draw(screen)

    def update(self):
        self.bottles.update()

        if random.randrange(self.bottle_density) != 0: return
        
        bot = Bottle()
        self.bottles.add(bot)

