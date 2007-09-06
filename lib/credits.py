'''score releted stuff'''

import os
import pickle
import sys
import math

import config
import utils
import pygame
from pygame.locals import *

from time import sleep


class Credits(object):

    def __init__(self, screen, father=None, score=-1):
        self.screen = screen
        self.father = father

    def loop(self):
        pass
        

    def draw_screen(self, text_list):

        pygame.display.set_caption(config.WINDOW_TITLE)
        background = utils.load_image(config.BGIMAGE1)

        font1 = pygame.font.Font(config.FONT2, 40)
        font2 = pygame.font.Font(config.FONT2, 20)
        clock = pygame.time.Clock()

        title = text_list[0]
        text_list.remove(title)

        title_img = font1.render(title, True, config.RED)
        topleft = (background.get_rect().width - title_img.get_rect().width) / 2, 30
        background.blit(title_img, topleft)
        bg = background.copy()

        self.screen.blit(background, (0, 0))
        pygame.display.flip()

        hor_step = font2.get_height()
        done = False
        timeloop = 0
        state = 0

        while not done:
            clock.tick(config.CLOCK_TICS)
            pygame.display.flip()
            self.screen.blit(background, (0, 0))
            y = hor_step + 100

            timeloop += 1
            if timeloop == config.CLOCK_TICS:
                state = 1
                done = True

            for i,text_item in enumerate(text_list):
                img = font2.render(text_item, True, config.RED)
                x2 = self.screen.get_width()/2
                if (state == 0) and (i%2 == 0):
                    x1 = x2 - ((config.width * 0.86) * (50 - timeloop) / 50)
                elif (state == 0) and (i%2 == 1):
                    x1 = x2 + ((config.width * 0.86) * (50 - timeloop) / 50)
                else:
                    x1=x2
                    bg.blit(img, (x, y))
                x = (x1+(x2-x1)*(1-math.exp(-timeloop/20.0)))
                x -= img.get_width()/2
                self.screen.blit(img, (x, y))
                y += hor_step + 15
        
        return bg

    def _waitKey(self):
        while 1:
            event = pygame.event.wait()
            if (event.type == QUIT) or (pygame.key.get_pressed()[K_RETURN]) or (pygame.key.get_pressed()[K_ESCAPE]):
                pygame.event.get()
                return self.father


