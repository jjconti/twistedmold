import pygame
from pygame.locals import *
import sys
import random
from sprites import *
import music
import utils
from hero import Hero
from moldsmanager import MoldsManager
from config import  *
from explotion import Explotion

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class Level(object):
    '''TwistedMold level'''
    
    def __init__(self, screen):
        self.screen = screen

        self.background = utils.create_surface((width, height), (0,0,0))
        self.screen.blit(self.background, (0, 0))
  	
    	#parameters
    	self.time_leap = 0.05
    	self.time_add = 5
    	self.mold_density_top_limit = 300
    	self.mold_density_bottom_limit = 10
    	self.mold_velocity = 30
	
        #Create the game clock
        self.clock = pygame.time.Clock()

        self.mm = MoldsManager(self.mold_density_top_limit, self.mold_density_bottom_limit,self.mold_velocity)
        self.points = 0
        self.pointsCounter = Points(0)
        self.tics = 0
	 
        self.timeBar = TimeBar(self.time_leap)

        self.gadgets = pygame.sprite.RenderUpdates()
        self.gadgets.add(self.pointsCounter)
        self.gadgets.add(self.timeBar)
	
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
        self.explotion = Explotion()	

    def loop(self):  

        while True:
            self.tics += 1     
            self.screen.blit(self.background, (0,0)) 
            self.update()
            self.draw()

            #Control
            for event in pygame.event.get():
                self.control(event)

            self.clock.tick(50)
            pygame.display.flip()

    def update(self):
        self.timeBar.update(self.tics)
        self.mm.gen(self.tics)
        self.mm.move(self.tics)
        #Blood Explotion
        self.explotion.update(self.tics, self.screen)
 
        #Verify collision
        if self.mm.fit(self.hero.group, self.tics):
            self.explotion.boom(self.hero.parts['cheat'].rect)
            self.pointsCounter.add_positive()
            self.timeBar.add_time(self.time_add)
	
    def draw(self):
        self.gadgets.draw(self.screen)
        self.mm.draw(self.screen)
        self.hero.group.draw(self.screen)	

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
                music.play_scream()
                       

def main():
    Level().loop()

if __name__ == "__main__":
    main()