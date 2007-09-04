import pygame
from pygame.locals import *
import sys
import random
from sprites import *
from sprites import BloodDrop
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


        
        #self.screen.blit(self.background, (0,0))
        #tit_color = (40,40,40)
        #title_img = font_title.render('PRUEBA', True, tit_color)
        #topleft = (background.get_rect().width - title_img.get_rect().width) / 2, 30
        #bg = self.background.copy()
        #bg.blit(title_img, topleft)
        #self.background = bg        

        
        #Create the game clock
        self.clock = pygame.time.Clock()

        self.mm = MoldsManager()
        self.points = 0
        self.pointsCounter = Points(0)
        self.tics = 0
        self.max_time = 1000.0
        self.time = (self.max_time - self.tics) / self.max_time
        self.timeBar = TimeBar(self.time)

        self.gadgets = pygame.sprite.RenderUpdates()
        self.gadgets.add(self.pointsCounter)
        self.gadgets.add(self.timeBar)

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




        #Set blood effect
        self.blood = pygame.sprite.RenderUpdates()
        explotion = False	
        blood_flag = 0 
        for x in xrange(333):	
            blood_drop = BloodDrop()
            self.blood.add(blood_drop)

        while self.time > 0:
            self.tics += 1            
            self.time = (self.max_time - self.tics) / self.max_time

            
            self.timeBar.update(self.time)
            self.mm.gen(self.tics)
            self.mm.move(self.tics)
            
            self.screen.blit(self.background, (0,0)) 


            #Blood Explotion
            if explotion:
                self.blood.update(self.tics)
                self.blood.draw(self.screen)
                blood_flag += 1             
            
            if blood_flag == 50:
                explotion = False
 
            #Verify collision
            if self.mm.fit(self.hero.group, self.tics):

                self.points += 1
                self.pointsCounter.update(self.points)

                blood_flag = 0
                explotion = True
                self.pointsCounter.add_positive()
                for blood_drop in self.blood:
                    blood_drop.set_position(self.hero.parts['cheat'].rect.top, self.hero.parts['cheat'].rect.left)

            #Draw
            self.gadgets.draw(self.screen)
            self.mm.draw(self.screen)
            self.hero.group.draw(self.screen)

            #Control
            for event in pygame.event.get():
                self.control(event)

            self.clock.tick(50)
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
                       

def main():
    Level().loop()

if __name__ == "__main__":
    main()
