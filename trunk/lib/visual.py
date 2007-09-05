import pygame
import time
from pygame.locals import *

class Visual(object):
    def __init__(self, screen, images, time, func):
        
        self.screen = screen
        self.images = images
        self.time = time
        self.func = func

    def loop(self):
        for image in images:
            self.screen.blit(image, (0,0))
            pygame.display.flip()
            time.sleep(self.time)
        return self.func

if __name__ == '__main__':
    print 'main'
    def prueba():
        print 'funcion devuelta'

    pygame.init()
    size = (700,550)
    screen = pygame.display.set_mode(size)
    fill = [(0,0,0), (255,255,255), (127,127,127), (50,50,50)]
    images = []
    for x in range(4):
        image = pygame.Surface(screen.get_size())
        image = image.convert()
        image.fill(fill[x])
        images.append(image)
    visual = Visual(screen, images, 1, prueba)
    func = visual.loop()
    func()
