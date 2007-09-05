import pygame
import random
from sprites import BloodDrop
import utils
from config import *

class Explotion(object):

    def __init__(self):
        self.blood = pygame.sprite.RenderUpdates()
        self.explotion = False	
        self.blood_flag = 0 
        for x in xrange(333):	
            blood_drop = BloodDrop()
            self.blood.add(blood_drop)

    def update(self, tics, screen):
        if self.explotion:
            self.blood.update(tics)
            self.blood.draw(screen)
            self.blood_flag += 1             
            
        if self.blood_flag == 50:
            explotion = False

    def boom(self, rect):
        self.blood_flag = 0
        self.explotion = True	
	     
        for blood_drop in self.blood:
            blood_drop.set_position(rect.top,rect.left)
