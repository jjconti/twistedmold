import pygame
from pygame.locals import *
import sys
import random
from sprites import Part
import utils
from hero import Hero
from moldsmanager import MoldsManager
from config import  *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class Level(object):
    '''TwistedMold level'''
    
    def __init__(self):
        #Initialize 
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(WINDOW_TITLE)

        self.background = utils.create_surface((width, height), (0,0,0))
        self.screen.blit(self.background, (0, 0))

        #Create the game clock
        self.clock = pygame.time.Clock()

        self.mm = MoldsManager()

        self.gameover = False
        
    def loop(self):  

        #Create the hero parts
        rhand = Part(lit='a', numb=1, top=center, left=0)
        head = Part(lit='b', numb=1, top=center, left=2 * side)
        lhand = Part(lit='c', numb=1, top=center, left=4 * side)
        rarm = Part(lit='d', numb=1, top=center + side, left=0)
        rshould = Part(lit='e', numb=1, top=center + side, left=side)
        cheat = Part(lit='f', numb=1, top=center + side, left=2 * side)
        lshould = Part(lit='g', numb=1, top=center + side, left=3 * side)
        larm = Part(lit='h', numb=1, top=center + side, left=4 * side)
        legs = Part(lit='i', numb=1, top=center + 2 * side, left=2 * side)
        foots = Part(lit='j', numb=1, top=center + 3 * side, left=2 * side)

        parts = dict(rhand=rhand, head=head, lhand=lhand, rarm=rarm, rshould=rshould, \
                            cheat=cheat, lshould=lshould, larm=larm, legs=legs, foots=foots)

        self.hero = Hero(pygame.sprite.RenderUpdates(), parts)

        times = 0

        while not self.gameover:

    
            while True:
                times += 1
                self.mm.gen(times)

                self.clock.tick(50)
                self.screen.blit(self.background, (0,0)) 
                self.mm.move()
                self.mm.draw(self.screen)

                self.hero.group.draw(self.screen)

                for event in pygame.event.get():
                    self.control(event)
                
                pygame.display.flip()


    def control(self, event):
        
        if event.type == QUIT:
            sys.exit(0)

        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                self.hero.down()
            if event.key == K_UP:
                self.hero.up()
            if event.key == K_RIGHT:
                self.hero.right()
            if event.key == K_LEFT:
                self.hero.left()
            if event.key == K_SPACE:
                self.hero.twist()
                       



if __name__ == "__main__":
    Level().loop()
