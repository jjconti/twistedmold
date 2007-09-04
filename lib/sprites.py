import pygame
import os
from utils import *
from config import *

class Part(pygame.sprite.Sprite):

    def __init__(self, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.lit = kwargs['lit']
        self.numb = kwargs['numb']
        self.image = load_image(os.path.join(parts, self.lit + str(self.numb) + ".png"))
        self.rect = self.image.get_rect(top=kwargs['top'], left=kwargs['left'])

    def __str__(self):
        return "Parte"

    def move(self):
        '''From right to left'''
        self.rect.move_ip(-1, 0)
        
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

