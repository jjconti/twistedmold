import pygame
import time
from pygame.locals import *

class Visual(object):
    def __init__(self, screen, images, times, func):
        
        self.screen = screen
        self.images = images
        self.times = times
        self.func = func

    def loop(self):
        for image, time_sleep in zip(self.images, self.times):
            self.screen.blit(image, (0,0))
            pygame.display.flip()
            time.sleep(time_sleep)
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
    times = [0.2,1.2,6.3,3]
    visual = Visual(screen, images, times, prueba)
    func = visual.loop()
    func()
