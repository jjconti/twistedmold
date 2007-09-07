import pygame
import random
from sprites import Part
from twist import twist
import utils
from config import *
import music
import math

class MoldsManager(object):

    def __init__(self, mold_density, mold_velocity):
        self.molds = []
        self.mold_density = mold_density
        self.mold_velocity = mold_velocity
        self.tops = [25, 125, 250, 375]
        self.destroy_all_flag = False
        self.destroy_all_finish = 0


    def move(self, times):
    
        if self.destroy_all_finish == 40:
            self.destroy_all_flag = False
            self.destroy_all_finish = 0
            
        
        if self.destroy_all_flag:
            self.expansion_radius = self.destroy_all_finish*15+20 
            x,y = self.destroy_all_center
            temp = []                       
            for m in self.molds:
                for part in m:
                    (xp,yp) = part.rect.top, part.rect.left
                    distance = math.sqrt(math.pow( (xp - x), 2) + math.pow( (yp - y), 2))
                    if distance < self.expansion_radius:
                        temp.append(m)
                        break
                    
            for t in temp:
                self.level.pos_points += 1
                self.molds.remove(t)
                del t
                    
        
        if times % self.mold_velocity != 0: return
    
        for m in self.molds:
            for part in m:
                part.move()
        #delete old mold
            if max(r.rect.right for r in m) < 0:
                self.level.neg_points += 1
                self.molds.remove(m)
                del m

    def draw(self, screen):
        if self.destroy_all_flag:
            self.destroy_all_finish += 1
            x,y = self.destroy_all_center
            circle = pygame.draw.circle(screen, (240,251,227),(y,x),self.expansion_radius, 20)

        for m in self.molds:
            m.draw(screen)

    def destroy_all(self, destroy_all_center):
        self.destroy_all_flag = True
        self.destroy_all_center = destroy_all_center

    def gen(self, times):

        if random.randrange(self.mold_density) != 0: return

        #Create mold blocks
        top = random.choice(self.tops)

        rhand = Part(lit='k', numb=1, top=top, left=WIDTH)
        head = Part(lit='k', numb=1, top=top, left=WIDTH + 2 * SIDE)
        lhand = Part(lit='k', numb=1, top=top, left=WIDTH + 4 * SIDE)
        rarm = Part(lit='k', numb=1, top=top + SIDE, left=WIDTH)
        rshould = Part(lit='k', numb=1, top=top + SIDE, left=WIDTH + SIDE)
        cheat = Part(lit='k', numb=1, top=top + SIDE, left=WIDTH + 2 * SIDE)
        lshould = Part(lit='k', numb=1, top=top + SIDE, left=WIDTH + 3 * SIDE)
        larm = Part(lit='k', numb=1, top=top + SIDE, left=WIDTH + 4 * SIDE)
        legs = Part(lit='k', numb=1, top=top + 2 * SIDE, left=WIDTH + 2 * SIDE)
        foots = Part(lit='k', numb=1, top=top + 3 * SIDE, left=WIDTH + 2 * SIDE)

        blocks = dict(rhand=rhand, head=head, lhand=lhand, rarm=rarm, rshould=rshould, \
                            cheat=cheat, lshould=lshould, larm=larm, legs=legs, foots=foots)

        mold = pygame.sprite.RenderUpdates()
        mold.add(blocks.values())
        
        #Avoid molds overlaping
        for m in self.molds:
            d = pygame.sprite.groupcollide(mold, m, False, False)
            if len(d):
                del mold
                return         
    
        for i in xrange(0,random.randrange(0, 6)):
            twist(blocks, i)
    
        self._add(mold)

    def _add(self, m):
        self.molds.append(m)

    def _remove(self, m):
        self.molds.remove(m)

    def fit(self, hero, times):
        '''Ask if the hero fit any mold and remove the fitted mold.'''
        for m in self.molds:
            if hero.fit(m):
                self.molds.remove(m)
                m.empty()
                del m
                music.play_bloop()
                return True
            
        return False

