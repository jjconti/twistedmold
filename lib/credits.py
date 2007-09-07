'''score releted stuff'''

import math
import pygame
from pygame.locals import *

from config import *
import utils
import music

class Credits(object):

    def __init__(self, screen, father=None):
        self.screen = screen
        self.father = father
        self.credits = []

    def loop(self):
        music.play_music(CREDITSMUSIC)
        self._load_credits()
        self._draw_screen()
        return self._waitKey()

    def _load_credits(self):
        try:
            f=open(CREDITS,'r')
            aux=f.read()
            f.close()
            aux=aux.split('\n')[:-2]
            for item in aux:
                self.credits.append(item.split(','))
            #self._convert()
        except IOError:
            print 'Cannot open credits file'

    def _convert(self):
        for item in self.credits:
            while len(item[0])<len(item[1]):
                item[0]=" "+item[0]+" "
            while len(item[1])>len(item[0]):
                item[1]=" "+item[1]+" "
        print self.credits    

    def _draw_screen(self):

        pygame.display.set_caption(WINDOW_TITLE)
        background = utils.load_image(CREDITIMAGE)

        font1 = pygame.font.Font(FONT3, 20)
        font2 = pygame.font.Font(FONT3, 40)
        clock = pygame.time.Clock()

        title = 'CREDITS'
        title_img = font2.render(title, True, WHITE)
        topleft = (background.get_rect().width - title_img.get_rect().width) / 2, 30
        background.blit(title_img, topleft)
 
        self.screen.blit(background, (0, 0))
        pygame.display.flip()

        done = False
        timeloop = 0
        state = 0
        y1 = 420
        y2 = 470    

        w = self.screen.get_width()
        
        for item in self.credits:
            img1 = font1.render(item[0], True, WHITE)
            img2 = font2.render(item[1], True, WHITE)
            self.screen.blit(background, (0, 0))
            pygame.display.flip()
            
            for i in range(w+img2.get_width()):
                x1 = i
                x2 = w-i
                if x1 == x2:
                    pygame.time.delay(1)
                x1 -= img1.get_width()/2
                x2 -= img2.get_width()/2
                if x1 == x2:
                    pygame.time.delay(2)
                self.screen.blit(img1, (x1, y1))
                self.screen.blit(img2, (x2, y2))
                pygame.display.flip()
                self.screen.blit(background, (0, 0))
                if pygame.event.peek([QUIT,K_RETURN,K_ESCAPE]):
                    return self.father

    def _waitKey(self):
        while 1:
            event = pygame.event.wait()
            if (event.type == QUIT) or (pygame.key.get_pressed()[K_RETURN]) or (pygame.key.get_pressed()[K_ESCAPE]):
                return self.father


