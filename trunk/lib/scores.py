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

MAX = 10 # max player number in highscore screen 
CPL = 15 # max char per line
SCORE_HUMAN = 1000 # you begin to be human
SCORE_DEAD = 500 # you is happy dead

class HighScores(object):

    def __init__(self, screen, father=None, score=-1):
        self.screen = screen
        self.father = father
        self.score = score
        self.top_scores = []
        self.font1 = pygame.font.Font(config.FONT3, 40)
        self.font2 = pygame.font.Font(config.FONT3, 30)

    def loop(self):
        if (not os.path.exists(config.HISCORES)) and (self.score <= 0):
            text_list=["HIGH SCORE","I\'m sorry","Nobody has been saved.","Nobody has stopped being zombie"]
            self.draw_screen(text_list)
            return self._waitKey()
        else:
            self.top_scores = self._load_score()
            if self.score > 0:
                self._add()
            text_list = self._convert()
            text_list[0:0]=['HIGH SCORES']
            self.draw_screen(text_list)
            return self._waitKey()

    def _add(self):
        #Check minor_value before adding
        top = self.top_scores
        for i in range(MAX):
            if self.score > top[i][1]:
                name = InputPanel(self.screen,self.score).loop()
                self.top_scores = top[:i] + [(name, self.score)] + top[i:-1]
                break
        f = file(config.HISCORES, 'w')
        pickle.dump(self.top_scores,f)

    def _load_score(self):
        top_scores = []
        if not os.path.exists(config.HISCORES):
            top_scores = [("", 0),
                            ("", 0),
                            ("", 0),
                            ("", 0),
                            ("", 0),
                            ("", 0),
                            ("", 0),
                            ("", 0),
                            ("", 0),
                            ("", 0),]
            f = file(config.HISCORES, 'w')
            pickle.dump(top_scores, f)
        else:
            f = file(config.HISCORES)
            top_scores = pickle.load(f)
        return top_scores

    def _convert(self):
        top10 = []
        for i,element in enumerate(self.top_scores):
            if element[1] != 0:
                if element[1] >= SCORE_HUMAN:
                    kind=" (HUMAN)"
                elif element[1] >= SCORE_DEAD:
                    kind=" (HAPPY DEAD)"
                else:
                    kind=""
                top10.append(str(i+1) + " " + element[0] + "  " + str(element[1]) + kind)
        return top10

    def draw_screen(self, text_list):

        pygame.display.set_caption(config.WINDOW_TITLE)
        background = utils.load_image(config.BGIMAGE1)

        clock = pygame.time.Clock()

        title = text_list[0]
        text_list.remove(title)

        title_img = self.font1.render(title, True, config.RED)
        topleft = (background.get_rect().width - title_img.get_rect().width) / 2, 25
        background.blit(title_img, topleft)
        bg = background.copy()

        self.screen.blit(background, (0, 0))
        pygame.display.flip()

        hor_step = self.font2.get_height()
        done = False
        timeloop = 0
        state = 0

        while not done:
            clock.tick(config.CLOCK_TICS)
            pygame.display.flip()
            self.screen.blit(background, (0, 0))
            y = hor_step + 80

            timeloop += 1
            if timeloop == config.CLOCK_TICS:
                state = 1
                done = True

            for i,text_item in enumerate(text_list):
                img = self.font2.render(text_item, True, config.RED)
                x2 = self.screen.get_width()/2
                if (state == 0) and (i%2 == 0):
                    x1 = x2 - ((config.width * 0.86) * (50 - timeloop) / 50)
                elif (state == 0) and (i%2 == 1):
                    x1 = x2 + ((config.width * 0.86) * (50 - timeloop) / 50)
                else:
                    x1=x2
                x = (x1+(x2-x1)*(1-math.exp(-timeloop/20.0)))
                x -= img.get_width()/2
                self.screen.blit(img, (x, y))
                if x1 == x2:
                    bg.blit(img, (x, y))
                y += hor_step + 10
        
        return bg

    def _waitKey(self):
        while 1:
            event = pygame.event.wait()
            if (event.type == QUIT) or (pygame.key.get_pressed()[K_RETURN]) or (pygame.key.get_pressed()[K_ESCAPE]):
                pygame.event.get()
                return self.father


class InputPanel(object):
    '''A generic input panel.'''

    def __init__(self, screen, score):
        self.screen = screen
        self.cursor = '|'
        self.text = ""
        self.done = False
        self.font1 = pygame.font.Font(config.FONT3, 40)
        self.clock = pygame.time.Clock()

        score_text="Your score is "+str(score)
        text_list=["CONGRATULATION !!!","WELCOME TO THE \"HALL OF FAME\"","Please, introduces your name","  ",score_text]
        print text_list
        self.background = HighScores(screen).draw_screen(text_list)
        pygame.display.flip()
        
        self._draw_text()

    def loop(self):
        while not self.done:
            self.clock.tick(config.CLOCK_TICS)
            self.screen.blit(self.background, (0,0))    

            for event in pygame.event.get():
                self.control(event)

            self._draw_text()
            pygame.display.flip()

        return self.text

    def control(self, event):
        if event.type == QUIT:
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key in (K_RETURN, K_KP_ENTER):
                self.enter()
            else:
                char = event.unicode
                if (self.valid_char(char)) and (len(self.text) < CPL):
                    self.text += char
                    self._draw_text()
                if event.key == K_BACKSPACE:
                    self.text = self.text[:-1]
                    self._draw_text()

    def valid_char(self, char):
        if char:
            if char in u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ1234567890":
                return True
        return False
               
    def enter(self):
        self.done = True

    def _draw_text(self):
        y = 300 # Tune this value as you need
        text_img = self.font1.render(self.text + self.cursor, True, config.RED)
        x = (self.screen.get_width() - text_img.get_width()) / 2
        self.screen.blit(text_img, (x,y))

