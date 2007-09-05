import pygame
import random
from sprites import Part
from twist import twist
import utils
from config import *

class MoldsManager(object):

    def __init__(self, mold_density_tl, mold_density_bl, mold_velocity):
        self.molds = []
	self.mold_density_tl = mold_density_tl
	self.mold_density_bl = mold_density_bl
	self.mold_velocity = mold_velocity
        self.tops = [25, 125, 250, 375]
        self.SOUND = {}
        self.SOUND['eat'] = utils.load_sound(BLOOP)

    def move(self, times):
        if times % self.mold_velocity != 0: return
	
        for m in self.molds:
            for part in m:
                part.move()
	        #delete old mold
            if max(r.rect.right for r in m) < 0:
                print "delete"
		self.molds.remove(m)
                del m

    def draw(self, screen):
        for m in self.molds:
            m.draw(screen)

    def gen(self, times):

        if times % random.randrange(self.mold_density_bl,self.mold_density_tl) != 0: return

        #Create mold blocks
        top = random.choice(self.tops)

        rhand = Part(lit='k', numb=1, top=top, left=width)
        head = Part(lit='k', numb=1, top=top, left=width + 2 * side)
        lhand = Part(lit='k', numb=1, top=top, left=width + 4 * side)
        rarm = Part(lit='k', numb=1, top=top + side, left=width)
        rshould = Part(lit='k', numb=1, top=top + side, left=width + side)
        cheat = Part(lit='k', numb=1, top=top + side, left=width + 2 * side)
        lshould = Part(lit='k', numb=1, top=top + side, left=width + 3 * side)
        larm = Part(lit='k', numb=1, top=top + side, left=width + 4 * side)
        legs = Part(lit='k', numb=1, top=top + 2 * side, left=width + 2 * side)
        foots = Part(lit='k', numb=1, top=top + 3 * side, left=width + 2 * side)

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
            d = pygame.sprite.groupcollide(hero, m, False, False)
            if len(d) == 10:
		self.molds.remove(m)
                m.empty()
		del m
                self.SOUND['eat'].play()

                return True
            
        return False

