import pygame
from pygame.locals import *

class Visual(object):
    def __init__(self, screen, images, times, func=None):
        self.screen = screen
        self.images = images
        self.times = [x*1000 for x in times]
        self.func = func    #father function

    def loop(self):
        for image, time_sleep in zip(self.images, self.times):
            self.screen.blit(image, (0,0))
            pygame.display.flip()
            i = 1
            while i < time_sleep:
                pygame.time.delay(1)
                i += 1
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        return self.func
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
    # time in milisecons
    times = [950,700,650,800]
    visual = Visual(screen, images, times, prueba)
    func = visual.loop()
    func()