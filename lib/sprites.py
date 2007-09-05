import pygame
import os
import utils
from config import *
import random
import math



class Points(pygame.sprite.Sprite):
    
    def __init__(self, points):
        pygame.sprite.Sprite.__init__(self)
        self.positive_points = points
        self.negative_points = points
        self.font = pygame.font.Font(FONT1, 35)
        self.image = self._image()
        self.rect = self.image.get_rect(top=0, right=width - 1)

    def add_positive(self):
        self.positive_points += 1
        self.image = self._image()
        self.rect = self.image.get_rect(top=0, right=width - 1)

    def add_negative(self):
        self.negative_points += 1
        #self.image = self._image()        
     
    def _image(self):
        return self.font.render("Points: " + str(self.positive_points), True, COLOR1)


class EnergyBar(pygame.sprite.Sprite):
    '''A tiem bar'''
    def __init__(self, time_leap):
        pygame.sprite.Sprite.__init__(self)
        self.energy_leap = time_leap
        self.energy_percent = 100 #percent remanding of time
        self.image = self._image()
        self.rect = self.image.get_rect(bottom=height - 1, left=0)

    def update(self, tics):
        self.energy_percent -= self.energy_leap
        self.image = self._image()

    def add_energy(self, add_percent):
	self.energy_percent += add_percent
        
    def _image(self):
        h = 15
        w = int(width * self.energy_percent / 100)
        if self.energy_percent > 60: 
            color = GREEN
        elif self.energy_percent > 30:
            color = ORANGE
        else:
            color = RED
        return utils.create_surface((w,h), color)

class LevelTime(pygame.sprite.Sprite):
    '''A tiem bar'''
    def __init__(self, seconds=270):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(FONT1, 35)
        self.seconds = seconds 
        self.image = self._image()
        self.rect = self.image.get_rect(left=3, top = 2)

    def update(self, tics):
        if tics % CLOCK_TICS: return 
        self.seconds -= 1
        self.image = self._image()

    def _image(self):
        return self.font.render("TIME: " + str(self.seconds), True, COLOR1)
    
class Part(pygame.sprite.Sprite):

    def __init__(self, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.lit = kwargs['lit']
        self.numb = kwargs['numb']
        self.image = utils.load_image(os.path.join(parts, self.lit + str(self.numb) + ".png"))
        self.rect = self.image.get_rect(top=kwargs['top'], left=kwargs['left'])

    def __str__(self):
        return "Parte"

    def move(self):
        '''From right to left'''
        self.rect.move_ip(-side, 0)
        
    def right(self):
        self.rect.move_ip(side, 0)
 
    def left(self):
        self.rect.move_ip(-side, 0)        

    def up(self):
        self.rect.move_ip(0, -side)

    def down(self): 
        self.rect.move_ip(0, side)

    def twist(self, x, y, rot=0, flipx=False, flipy=False):
        '''x,y: offsets, rot: deegrees rotation'''
        self.rect.top += x
        self.rect.left += y 
        self.image = pygame.transform.rotate(self.image, rot)
        self.image = pygame.transform.flip(self.image, flipx, flipy)


class BloodDrop(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = utils.load_image(DROP)
        self.rect = self.image.get_rect()
	
    def update(self, times):
        if times % 2 != 0: return
        self.x += self.vx
        self.y += self.vy
        self.vy += 1
        self.rect.left = self.x
        self.rect.top = self.y
        
    def set_position(self, top, left):
    	ang = random.randrange(0,3600)/10.0
        ang = math.pi * ang / 180.0
    	vel = random.randrange(50,250)/10.0
        self.vx = math.cos(ang) * vel
        self.vy = math.sin(ang) * vel
        self.x = left
        self.y = top
        self.rect.left = left
        self.rect.top = top

