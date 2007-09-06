import pygame
import random
from sprites import Bottle
from twist import twist
import utils
from config import *
import music

class BottleManager(object):
    energy = dict(good=10, bad=-10)

    def __init__(self):
        self.bottles = pygame.sprite.Group()
        self.bottle_density = 33
        self.bottles.add(Bottle(random.choice(range(10))))

    def draw(self, screen):
        self.bottles.draw(screen)

    def update(self):
        
        self.bottles.update()
        self.impact()

        if random.randrange(self.bottle_density) != 0: return
        
        bot = Bottle(random.choice(range(-10, 10)))
        self.bottles.add(bot)

    def impact(self):
        d = pygame.sprite.groupcollide(self.bottles,self.hero.group, True, False)
        if d:
            for bottle in d.keys():
                self.energy_bar.add_energy(bottle.energy)    

