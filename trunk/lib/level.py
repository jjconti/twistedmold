import pygame
from pygame.locals import *
import sys
import random
from sprites import *
import music
import utils
from hero import Hero
from moldsmanager import MoldsManager
from bottlemanager import BottleManager
from config import  *
from explotion import Explotion
from wheather import Wheather
from menu import Menu

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class Level(object):
    '''TwistedMold level'''
    
    '''mold_density_tl y mold_density_bl. Mientras mas bajos mas mold aparecen, mientras mas separados mas disperso'''

    def __init__(self, screen, father, energy_leap=0.07, energy_add=5, mold_density=30, mold_velocity=30):
        self.screen = screen
        self.father = father

        self.background = utils.load_image(BGIMAGE2)
        #self.screen.blit(self.background, (0, 0))
  	
    	#parameters
    	self.energy_leap = energy_leap
    	self.energy_add = energy_add
    	self.mold_density = mold_density
    	self.mold_velocity = mold_velocity

        #menu control
        self.options = [("Yes", self.father),("No", None)]
        self.game_over = False
	
        #Create the game clock
        self.clock = pygame.time.Clock()

        self.mm = MoldsManager(self.mold_density, self.mold_velocity)
        self.bm = BottleManager()
        self.bm.mm = self.mm

        self.points = 0
        self.pointsCounter = Points(0)
        self.mm.pointsCounter = self.pointsCounter        

        self.tics = 0

        self.snow_slim = pygame.sprite.Group()
        self.snow_fat = pygame.sprite.Group()        

        for x in range(75):
            sprite = Wheather(1,2)
            self.snow_slim.add(sprite)

        for x in range(75):
            sprite = Wheather(3,5)
            self.snow_fat.add(sprite)
	 
        self.energy_bar = EnergyBar(self.energy_leap)
        self.bm.energy_bar = self.energy_bar

        self.level_time = LevelTime()

        self.gadgets = pygame.sprite.RenderUpdates()
        self.gadgets.add(self.pointsCounter)
        self.gadgets.add(self.energy_bar)
        self.gadgets.add(self.level_time)
	
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
        self.bm.hero=self.hero

        self.explotion = Explotion()

        self.control_down = -1
        self.control_up = -1
        self.control_left = -1
        self.control_right = -1
        self.control_tiempo = 5

    def loop(self):  
        while not self.finnish():
            self.tics += 1     
            self.screen.blit(self.background, (-(self.tics % 700),0)) 
            self.update()
            self.draw()

            #Control
            for event in pygame.event.get():
                self.control(event)

            self.clock.tick(CLOCK_TICS)

            if self.control_down == 0: self.hero.down()
            if self.control_up == 0: self.hero.up()
            if self.control_right == 0: self.hero.right()
            if self.control_left == 0: self.hero.left()

            if self.control_down >= 0:
                self.control_down += 1
                if self.control_down >= self.control_tiempo:
                    self.control_down = 0
                    
            if self.control_up >= 0:
                self.control_up += 1
                if self.control_up >= self.control_tiempo:
                    self.control_up = 0

            if self.control_right >= 0:
                self.control_right += 1
                if self.control_right >= self.control_tiempo:
                    self.control_right = 0

            if self.control_left >= 0:
                self.control_left += 1
                if self.control_left >= self.control_tiempo:
                    self.control_left = 0

            self.clock.tick(CLOCK_TICS)

            pygame.display.flip()
    
        if self.game_over:
            return self.father
        elif not self.level_time:
            return self.father #hay que preguntar si paso de nivel y mandarlo al proxino sino gameover
        elif not self.energy_bar:
            return self.father #gameover

    def update(self):
        self.snow_slim.update()
        self.snow_fat.update()        

        self.energy_bar.update(self.tics)
        self.level_time.update(self.tics)

        self.bm.update()        

        self.mm.gen(self.tics)
        self.mm.move(self.tics)
        #Blood Explotion
        self.explotion.update(self.tics, self.screen)
 
        #Verify collision
        if self.mm.fit(self.hero.group, self.tics):
            self.explotion.boom(self.hero.parts['cheat'].rect)
            self.pointsCounter.add_positive()
            
	
    def draw(self):
        self.snow_slim.draw(self.screen)
        
        self.bm.draw(self.screen)
        self.mm.draw(self.screen)
        
        self.hero.group.draw(self.screen)
        self.snow_fat.draw(self.screen)	
        self.gadgets.draw(self.screen)

    def control(self, event):
        
        if event.type == QUIT:
            sys.exit(0)

        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                self.control_down = 0
            if event.key == K_UP:
                self.control_up = 0
            if event.key == K_RIGHT:
                self.control_right = 0
            if event.key == K_LEFT:
                self.control_left = 0
            if event.key == K_SPACE:
                self.hero.twist()
                music.play_scream()

            if event.key == K_ESCAPE:
                mem = Menu(self.screen, self.options, "Do you want to exit?").loop()
                if mem == self.father:
                    self.game_over = True

        if event.type == KEYUP:
            if event.key == K_DOWN:
                self.control_down = -1
            if event.key == K_UP:
                self.control_up = -1
            if event.key == K_RIGHT:
                self.control_right = -1
            if event.key == K_LEFT:
                self.control_left = -1

    def finnish(self):
        if self.level_time.seconds == 0 or self.energy_bar.energy_percent == 0 or self.game_over:
            return True
    
        return False


def main():
    Level().loop()

if __name__ == "__main__":
    main()
