import pygame
import random
from config import *
from sprites import Part
from twist import twist

class MoldsManager():

    def __init__(self):
        self.molds = []
        self.tops = [25, 125, 250, 375] 

    def move(self):
        for m in self.molds:
            for p in m:
                p.move()

    def draw(self, screen):
        for m in self.molds:
            m.draw(screen)

    def gen(self, times):

        if times % random.randrange(100,300) != 0: return

        print "Mold generado"
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
        for i in xrange(0,random.randrange(0, 6)):
            twist(blocks, i)
        self._add(mold)

    def _add(self, m):
        self.molds.append(m)

    def _remove(self, m):
        self.molds.remove(m)

    def fit(self, hero):
        '''Ask if the hero fit any mold and remove the fitted mold'''
        for m in self.molds:        
            d = pygame.sprite.groupcollide(hero, m, False, False)
            if len(d) == 10: print len(d), d
        
