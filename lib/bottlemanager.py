import pygame
import random
from sprites import Bottle
from twist import twist
import utils
from config import *
import music

class BottleManager(object):

    bottle1 = dict(energy=10, rotation=15, image=BOTTLE_BLUE, velocity=10) # azul
    bottle2 = dict(energy=-10, rotation=5, image=BOTTLE_GREEN, velocity=6) # verde
    bottle3 = dict(energy=25, rotation=30, image=BOTTLE_ORANGE, velocity=20) # naranja
    bottle4 = dict(energy=0, rotation=15, image=BOTTLE_RED, velocity=10, destroy_all=True) # roja

    def __init__(self, bottle1_density, bottle2_density, bottle3_density, bottle4_mount):
        self.bottles = pygame.sprite.Group()

        self.bottle_density = 50
        #self.bottles.add(Bottle(random.choice(range(10))))

        self.bottle1_density = bottle1_density
        self.bottle2_density = bottle2_density
        self.bottle3_density = bottle3_density
        self.bottle4_mount = bottle4_mount
        self.bottle4_current_mount = 0

        self.bottle1_flag = 0
        self.bottle2_flag = 0
        self.bottle3_flag = 0
        self.bottle4_flag = 0

        self.bottles.add(Bottle(self.bottle1))

    def draw(self, screen):
        self.bottles.draw(screen)

    def update(self):
        
        self.bottles.update()
        self.impact()

        if random.randrange(self.bottle1_density) == 0 and self.bottle1_flag: 
            bot = Bottle(self.bottle1)
            self.bottles.add(bot)
            self.bottle1_flag = CLOCK_TICS
        else:
            self.bottle1_flag -= 1

        if random.randrange(self.bottle2_density) == 0 and self.bottle1_flag: 
            bot = Bottle(self.bottle2)
            self.bottles.add(bot)
            self.bottle2_flag = CLOCK_TICS
        else:
            self.bottle2_flag -= 1

        if random.randrange(self.bottle3_density) == 0 and self.bottle1_flag: 
            bot = Bottle(self.bottle3)
            self.bottles.add(bot)
            self.bottle3_flag = CLOCK_TICS
        else:
            self.bottle3_flag -= 1

        if random.randrange(400) == 0 and self.bottle4_current_mount < self.bottle4_mount and self.bottle1_flag:
            bot = Bottle(self.bottle4)
            self.bottles.add(bot)
            self.bottle4_current_mount += 1
            self.bottle2_flag = CLOCK_TICS
        else:
            self.bottle4_flag -= 1
            
    def impact(self):
        d = pygame.sprite.groupcollide(self.bottles,self.hero.group, True, False)
        if d:
            for bottle in d.keys():
                self.energy_bar.add_energy(bottle.energy)
                if bottle.destroy_all:
                    self.mm.destroy_all((bottle.rect.top, bottle.rect.left))    

