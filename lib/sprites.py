import pygame
import os
import utils
from config import *

class Points(pygame.sprite.Sprite):
    
    def __init__(self, points):
        pygame.sprite.Sprite.__init__(self)
        self.points = points
        self.font = pygame.font.Font(FONT1, 35)
        self.image = self._image()
        self.rect = self.image.get_rect(top=0, right=width - 1)

    def update(self, points):
        self.points = points
        self.image = self._image()
        
    def _image(self):
        return self.font.render("Points: " + str(self.points), True, COLOR1)


class TimeBar(pygame.sprite.Sprite):
    '''A tiem bar'''
    def __init__(self, time):
        pygame.sprite.Sprite.__init__(self)
        self.time = time #percent remanding of time
        self.image = self._image()
        self.rect = self.image.get_rect(bottom=height - 1, left=0)

    def update(self, time):
        self.time = time
        self.image = self._image()
        
    def _image(self):
        h = 15
        w = int(width * self.time)
        if self.time > 0.6: 
            color = GREEN
        elif self.time > 0.3:
            color = ORANGE
        else:
            color = RED
        return utils.create_surface((w,h), color)

    
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

