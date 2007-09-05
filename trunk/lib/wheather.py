import pygame
from pygame.locals import *
import math
import sys
import random

class Wheather(pygame.sprite.Sprite):
    rang = range(5,21)
    gray_scale = range(170,255)

    func = [lambda x: 20*math.sin(x),
            lambda x: 20*math.cos(x)]

    
    def __init__(self,min_radius, max_radius):
        pygame.sprite.Sprite.__init__(self)

        self.radius = range(min_radius,max_radius)

        b = range(700)
        self.x = random.choice(b) 
        self.y= random.choice(b)

        self.image = pygame.Surface((8,8))
        self.image.set_colorkey((0,0,0))
        color = random.choice(self.gray_scale)
        gray_color = (color,color,color)
        pos = (4,4)
        radius = random.choice(self.radius)
        pygame.draw.circle(self.image, gray_color, pos, radius)
        self.rect = self.image.get_rect()
        self.num = self.count(random.randrange(5,12))

        self.func_x = random.choice(self.func)
        #print self.func_x
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        #print self.area.size

    def update(self):
        num = self.num.next()
        num = math.radians(num)
        func_y = 10*num
        #pos = (self.func_x(num,random.choice(self.rang)) + self.x, func_y + self.y)
        pos = (self.func_x(num) + self.x, func_y + self.y)
        self.rect.center = pos
        if self.rect.center[1] > self.area.size[1]:
            self.rect.center = (0,pos[1])
            self.num = self.count(random.randrange(5,12))
            self.y = 0

    def count(self,up):
        x = 0
        while 1:
            x = x+up
            yield x
