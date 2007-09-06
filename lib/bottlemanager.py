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
    image4 = "data//imgs//ball4.png"


    bottle1 = dict(energy=10, image=image1, velocity=5)
    bottle2 = dict(energy=-10, image=image2, velocity=3)
    bottle3 = dict(energy=25, image=image3, velocity=10)
    bottle4 = dict(energy=0, image=image4, velocity=10, destroy_all=True)

    def __init__(self, bottle1_density, bottle2_density, bottle3_density, bottle4_mount):
        self.bottles = pygame.sprite.Group()

        self.bottle_density = 50
        #self.bottles.add(Bottle(random.choice(range(10))))

        self.bottle1_density = bottle1_density
        self.bottle2_density = bottle2_density
        self.bottle3_density = bottle3_density
        self.bottle4_mount = bottle4_mount
        self.bottle4_current_mount = 0

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

        if random.randrange(400) == 0 and self.bottle4_current_mount < self.bottle4_mount: 
            bot = Bottle(self.bottle4)
            self.bottles.add(bot)
            self.bottle4_current_mount += 1
            
    def impact(self):
        d = pygame.sprite.groupcollide(self.bottles,self.hero.group, True, False)
        if d:
            for bottle in d.keys():
                self.energy_bar.add_energy(bottle.energy)
                if bottle.destroy_all:
                    self.mm.destroy_all()    

