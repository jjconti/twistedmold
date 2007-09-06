import pygame
import random
from sprites import Bottle
from twist import twist
import utils
from config import *
import music

class BottleManager(object):
    image1 = "data//imgs//ball.png"
    image2 = "data//imgs//ball2.png"
    image3 = "data//imgs//ball3.png"  

    bottle1 = dict(energy=10, image=image1)
    bottle2 = dict(energy=-10, image=image2)
    bottle3 = dict(energy=25, image=image3)

    def __init__(self):
        self.bottles = pygame.sprite.Group()
        self.bottle1_density = 500
        self.bottle2_density = 600
        self.bottle3_density = 1000

        self.bottles.add(Bottle(self.bottle1))

    def draw(self, screen):
        self.bottles.draw(screen)

    def update(self):
        
        self.bottles.update()
        self.impact()

        if random.randrange(self.bottle1_density) == 0: 
            bot = Bottle(self.bottle1)
            self.bottles.add(bot)

        if random.randrange(self.bottle2_density) == 0: 
            bot = Bottle(self.bottle2)
            self.bottles.add(bot)

        if random.randrange(self.bottle3_density) == 0: 
            bot = Bottle(self.bottle3)
            self.bottles.add(bot)

    def impact(self):
        d = pygame.sprite.groupcollide(self.bottles,self.hero.group, True, False)
        if d:
            for bottle in d.keys():
                self.energy_bar.add_energy(bottle.energy)    

