'''score releted stuff'''

import math
import pygame
from pygame.locals import *

from config import *
import utils
import music

from time import sleep

class Credits(object):

    def __init__(self, screen, father=None):
        self.screen = screen
        self.father = father
        self.credits = []
        self.font1 = pygame.font.Font(FONT3, 20)
        self.font2 = pygame.font.Font(FONT3, 40)
        self.font3 = pygame.font.Font(FONT3, 60)

    def loop(self):
        music.stop_music()
        music.play_music(CREDITSMUSIC)
        self._load_credits()
        self._draw_screen()
        pygame.time.delay(200)
        music.stop_music()
        return self.father
        #return self._waitKey()

    def _load_credits(self):
        try:
            f=open(CREDITS,'r')
            aux=f.read()
            f.close()
            aux=aux.split('\n')[:-2]
            for item in aux:
                self.credits.append(item.split(','))
        except IOError:
            print 'Cannot open credits file'

    def _draw_screen(self):
        pygame.display.set_caption(WINDOW_TITLE)
        background = utils.load_image(CREDITSIMAGE)

        clock = pygame.time.Clock()
        separator = 2

        title = 'CREDITS'
        title_img = self.font3.render(title, True, BLACK)
        title_img2 = self.font3.render(title, True, WHITE)
        topleft = (background.get_rect().width - title_img.get_rect().width) / 2, 30
        topleft2 = ((background.get_rect().width - title_img.get_rect().width) / 2)-separator, 30-separator
        background.blit(title_img2, topleft2)
        background.blit(title_img, topleft)
 
        self.screen.blit(background, (0, 0))
        pygame.display.flip()
        hor_step = self.font2.get_height()

        while 1:
            for text_list in self.credits:
                done = False
                timeloop = 0
                state = 0

                while not done:
                    clock.tick(CLOCK_TICS)
                    pygame.display.flip()
                    self.screen.blit(background, (0, 0))
                    y = hor_step + 380

                    timeloop += 1
                    if timeloop == CLOCK_TICS:
                        state = 1
                        done = True

                    for i,text_item in enumerate(text_list):
                        img = self.font2.render(text_item, True, BLACK)
                        img2 = self.font2.render(text_item, True, WHITE)
                        x2 = self.screen.get_width()/2
                        if (state == 0) and (i%2 == 0):
                            x1 = x2 - ((WIDTH * 0.86) * (50 - timeloop) / 50)
                        elif (state == 0) and (i%2 == 1):
                            x1 = x2 + ((WIDTH * 0.86) * (50 - timeloop) / 50)
                        else:
                            x1=x2

                        if self._verifyKey():
                            music.stop_music()
                            return self.father

                        x = (x1+(x2-x1)*(1-math.exp(-timeloop/20.0)))
                        x -= img.get_width()/2
                        self.screen.blit(img2, (x-separator, y-separator))
                        self.screen.blit(img, (x, y))
                        y += hor_step + 10

                #pygame.time.delay(250)
                if self._verifyKey():
                    music.stop_music()
                    return self.father

                done = False
                timeloop = CLOCK_TICS
                state = 1

                while not done:
                    clock.tick(CLOCK_TICS)
                    pygame.display.flip()
                    self.screen.blit(background, (0, 0))
                    y = hor_step + 380

                    timeloop -= 1
                    if timeloop == 0:
                        state = 0
                        done = True

                    for i,text_item in enumerate(text_list):
                        img = self.font2.render(text_item, True, BLACK)
                        img2 = self.font2.render(text_item, True, WHITE)
                        x2 = self.screen.get_width()/2
                        if (i%2 == 0):
                            x1 = (x2 + ((WIDTH * 0.86) * (50 - timeloop) / 50))
                        elif (i%2 == 1):
                            x1 = (x2 - ((WIDTH * 0.86) * (50 - timeloop) / 50))

                        if self._verifyKey():
                            music.stop_music()
                            return self.father

                        x = (x1+(x2-x1)*(1-math.exp(-timeloop/20.0)))
                        x -= img.get_width()/2
                        self.screen.blit(img2, (x-separator, y-separator))
                        self.screen.blit(img, (x, y))
                        y += hor_step + 10

                if self._verifyKey():
                    music.stop_music()
                    return self.father

    def _verifyKey(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if event.type == KEYDOWN and \
                (event.key in [K_ESCAPE, K_RETURN, K_KP_ENTER]):
                return True


