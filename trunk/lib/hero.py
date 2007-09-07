import pygame
from pygame import Rect
from config import *
from twist import twist
from sprites import HeroPart
import utils

class Hero(object):

    collision_matrix = (((1,0,1,0,1),  \
                         (1,1,1,1,1),  \
                         (0,0,1,0,0),  \
                         (0,0,1,0,0)), \
                        ((1,0,1,0,1),  \
                         (1,1,1,1,1),  \
                         (0,0,1,1,0),  \
                         (0,0,0,0,0)), \
                        ((1,0,1,0,0),  \
                         (1,1,1,1,1),  \
                         (0,0,1,1,1),  \
                         (0,0,0,0,0)), \
                        ((0,0,1,0,0),  \
                         (1,1,1,1,1),  \
                         (1,0,1,1,1),  \
                         (0,0,0,0,0)), \
                        ((0,0,1,0,1),  \
                         (1,1,1,1,1),  \
                         (1,1,1,0,0),  \
                         (0,0,0,0,0)), \
                        ((0,0,1,0,1),  \
                         (1,1,1,1,1),  \
                         (1,0,1,0,0),  \
                         (0,0,1,0,0)))

    def __init__(self):
        self.body_image = utils.load_image(os.path.join(BODY1), (255, 0, 255))
        self.parts = dict(head      =HeroPart(self.body_image, Rect(2*SIDE, 0*SIDE, 1*SIDE, 2*SIDE), (2, 0)), \
                          rhand_up  =HeroPart(self.body_image, Rect(0*SIDE, 0*SIDE, 2*SIDE, 2*SIDE), (0, 0)), \
                          rhand_down=HeroPart(self.body_image, Rect(0*SIDE, 3*SIDE, 2*SIDE, 2*SIDE), (0, 1)), \
                          lhand_up  =HeroPart(self.body_image, Rect(3*SIDE, 0*SIDE, 2*SIDE, 2*SIDE), (3, 0)), \
                          lhand_down=HeroPart(self.body_image, Rect(3*SIDE, 3*SIDE, 2*SIDE, 2*SIDE), (3, 1)), \
                          legs      =HeroPart(self.body_image, Rect(2*SIDE, 2*SIDE, 1*SIDE, 2*SIDE), (2, 2)), \
                          legs2left =HeroPart(self.body_image, Rect(3*SIDE, 2*SIDE, 2*SIDE, 1*SIDE), (2, 2)), \
                          legs2right=HeroPart(self.body_image, Rect(0*SIDE, 2*SIDE, 2*SIDE, 1*SIDE), (1, 2)))

        self.x = (LEVEL_LEFT)*SIDE
        self.y = (LEVEL_TOP+LEVEL_HEIGHT/2-2)*SIDE
        self.pos = 0
        self.group = pygame.sprite.Group()
        self.setup_parts()

    def up(self):
        if self.y > LEVEL_TOP*SIDE:
            self.y -= SIDE;
            self.setup_parts()

    def down(self):
        if self.y < (LEVEL_TOP+LEVEL_HEIGHT-4)*SIDE:
            self.y += SIDE;
            self.setup_parts()

    def left(self):
        if self.x > LEVEL_LEFT*SIDE:
            self.x -= SIDE;
            self.setup_parts()

    def right(self):
        if self.x < (LEVEL_LEFT+LEVEL_WIDTH-5)*SIDE:
            self.x += SIDE;
            self.setup_parts()

    def twist(self):
        #self.pos = twist(self.parts, self.pos)
        self.pos = (self.pos + 1) % 6
        self.setup_parts()

    def get_center(self):
        return (self.x+SIDE*2+HALF,self.y+SIDE*1+HALF)

    def setup_parts(self):
        self.group.empty()
        self.group.add(self.parts['head'])

        if self.pos == 0:
            self.group.add(self.parts['rhand_up'])
            self.group.add(self.parts['lhand_up'])
            self.group.add(self.parts['legs'])
        elif self.pos == 1:
            self.group.add(self.parts['rhand_up'])
            self.group.add(self.parts['lhand_up'])
            self.group.add(self.parts['legs2left'])
        elif self.pos == 2:
            self.group.add(self.parts['rhand_up'])
            self.group.add(self.parts['lhand_down'])
            self.group.add(self.parts['legs2left'])
        elif self.pos == 3:
            self.group.add(self.parts['rhand_down'])
            self.group.add(self.parts['lhand_down'])
            self.group.add(self.parts['legs2left'])
        elif self.pos == 4:
            self.group.add(self.parts['rhand_down'])
            self.group.add(self.parts['lhand_up'])
            self.group.add(self.parts['legs2right'])
        elif self.pos == 5:
            self.group.add(self.parts['rhand_down'])
            self.group.add(self.parts['lhand_up'])
            self.group.add(self.parts['legs'])

        for part in self.group:
            part.setup_rect(self.x, self.y)

    def fit(self, mold_group):
        xmin = WIDTH
        ymin = HEIGHT

        for m in mold_group:
            if xmin > m.rect.left: xmin = m.rect.left
            if ymin > m.rect.top: ymin = m.rect.top

        if xmin / SIDE != self.x / SIDE or \
           ymin / SIDE != self.y / SIDE:
            return False

        matrix = [[0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0]]
        for m in mold_group:
            matrix[(m.rect.top - ymin) / SIDE][(m.rect.left - xmin) / SIDE] = 1

        for y in range(0,4):
            for x in range(0,5):
                if matrix[y][x] != Hero.collision_matrix[self.pos][y][x]:
                    return False

        return True
