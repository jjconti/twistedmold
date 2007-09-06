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
from visual import Visual
from menu import Menu
from scores import HighScores

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

levels = {1: dict(energy_leap=0.05, mold_density=35, mold_velocity=10   , max_time=10, energy_add=5, img=LEVEL1),
          2: dict(energy_leap=0.1, mold_density=45, mold_velocity=15   , max_time=10, energy_add=5, img=LEVEL2),
          3: dict(energy_leap=0.1, mold_density=45, mold_velocity=15   , max_time=15, energy_add=5, img=LEVEL3),
          4: dict(energy_leap=0.1, mold_density=55, mold_velocity=20   , max_time=15, energy_add=5, img=LEVEL4)}
LEVELS = 4

class Level(object):
    '''TwistedMold level'''
    
    '''mold_density_tl y mold_density_bl. Mientras mas bajos mas mold aparecen, mientras mas separados mas disperso'''


    def __init__(self, screen, father, level, total_pos_points, total_neg_points):

        self.screen = screen
        self.father = father
        self.level = level
        self.background = utils.load_image(BGIMAGE2)
      
    	#parameters
    	self.energy_leap = levels[level]['energy_leap']
    	self.energy_add = levels[level]['energy_add']
    	self.mold_density = levels[level]['mold_density']
    	self.mold_velocity = levels[level]['mold_velocity']
        self.max_time = levels[level]['max_time']
        #menu control
        self.options = [("Yes", self.father),("No", None)]
        self.exit = False
	
        #Create the game clock
        self.clock = pygame.time.Clock()

        self.mm = MoldsManager(self.mold_density, self.mold_velocity)
        self.bm = BottleManager()
        self.bm.mm = self.mm

        self.total_pos_points = total_pos_points
        self.total_neg_points = total_neg_points

        self.pos_points = 0
        self.neg_points = 0
        
        
        self.pointsCounter = Points(0,0)
        self.mm.level = self
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

        self.level_time = LevelTime(self.max_time)

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

        #Show level image

        Visual(self.screen, [utils.load_image(levels[self.level]['img'])], [2], None).loop()

    def loop(self):  
        while not self.finish():
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
    
        if self.exit:
            return self.father
        elif not self.level_time.seconds:        
            if self.pos_points*1.0 / (self.pos_points*1.0 + self.neg_points*1.0) < 0.6:
                def f(screen):
                    return HighScores(screen, self.father).loop()
                return f
            
            if self.level < LEVELS:
                def f(screen):
                    return Level(screen, self.father, self.level + 1, self.total_pos_points + self.pos_points, self.total_neg_points + self.neg_points)
                return f
            else:
                print self.total_pos_points + self.pos_points #puntos positivos totales
                print self.total_neg_points + self.neg_points #puntos negativos totales
                
                print "definir una funcion que retorne una animacion de victoria"

                def f(screen):
                    return HighScores(self.screen, self.father, self.total_pos_points + self.pos_points)

                return f

        elif self.energy_bar.energy_percent <= 0:
            def f(screen):
                def g(screen):
                    return HighScores(self.screen, self.father, self.total_pos_points + self.pos_points) 
                music.play_gameover()
                return Visual(screen, [utils.load_image(GAMEOVER)], [3], g)               

            return f

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
            self.pos_points += 1

        self.pointsCounter.update(self.pos_points, self.neg_points)            
            
	
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
                mem = Menu(self.screen, self.options, "Do you want to quit?").loop()
                if mem == self.father:
                    self.exit = True

        if event.type == KEYUP:
            if event.key == K_DOWN:
                self.control_down = -1
            if event.key == K_UP:
                self.control_up = -1
            if event.key == K_RIGHT:
                self.control_right = -1
            if event.key == K_LEFT:
                self.control_left = -1

    def finish(self):
        if self.level_time.seconds == 0 or self.energy_bar.energy_percent <= 0 or self.exit:
            return True

        return False


def main():
    Level().loop()

if __name__ == "__main__":
    main()
