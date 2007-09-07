import pygame
from pygame.locals import *
import sys
import random

from sprites import *
import music
import utils
from hero import Hero
from moldsmanager import MoldsManager
from bottlemanager import BottleManager
from config import  *
from explotion import Explotion
from wheather import Wheather
from visual import Visual
from menu import Menu
from scores import HighScores

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

# bottle_density (azul, verde, naranja, roja_destroy)

'''
level 1:
    - la energia baja lento, de tal manera que siempre pasemos de nivel a menos
    que juguemos mal (comer bolas verdes)
    - 1 en 7000 posibilidades de que aparezca una naranja que te
    da mucha energia
    - los moldes vienen relativamente lento como para que no puedas hacer muchos
    puntos en este nivel que es mas facil
    - no hay bolas rojas que borran la pantalla
    - facil, para ser el primero tiene una buena complejidad (FACIL)

level 2:
    - no hay bolas rojas que borran la pantalla
    - mas posibilidades que aparezcan bolas naranjas con energia 1 en 400
    - aparecen mas moldes en el juego
    - el tiempo que hay que sobrevivir es el mismo al anterior
    - es un poco mas dificil que el anterior pero sigue entrando en la categoria
    de facil. Para pasarlo hay que comer un par de bolas de energia al menos

level 3:
    - permanecer mas tiempo vivo (se pone mas jodido)
    - los moldes se aceleran un poco
    - la energia se pierde mas rapido
    - es el mas divertido de los cuatro niveles
    - dificil, pero no tanto, como para pasarlo poniendole ganas

level 4:
    - la energia casi que la perdemos enseguida, necesitamos comer muchas
    naranjas y azules
    - es dificil, bastante
    - entretenido para ser el ultimo nivel (hay que jugarle un par de veces para
    ganar este nivel)
'''
levels = {1: dict(energy_leap=0.075, mold_density=55, mold_velocity=12,
                  max_time=15, img=LEVEL1, bottle_density=(400,550,7000,10)),
          2: dict(energy_leap=0.105, mold_density=40, mold_velocity=15,
                  max_time=15, img=LEVEL2, bottle_density=(500,300,400,0)),
          3: dict(energy_leap=0.13, mold_density=35, mold_velocity=15,
                  max_time=20, img=LEVEL3, bottle_density=(200,200,200,1)),
          4: dict(energy_leap=0.2, mold_density=27, mold_velocity=25,
                  max_time=25, img=LEVEL4, bottle_density=(250,100,100,1))}
LEVELS = 4

class Level(object):
    '''TwistedMold level'''

    def __init__(self, screen, father, level, total_pos_points, total_neg_points):

        self.screen = screen
        self.father = father
        self.level = level
        self.background = utils.load_image(BGIMAGE2)
      
        #parameters
        self.energy_leap = levels[level]['energy_leap']
        self.mold_density = levels[level]['mold_density']
        self.mold_velocity = levels[level]['mold_velocity']
        self.max_time = levels[level]['max_time']
        #menu control
        self.options = [("Yes", self.father),("No", None)]
        self.exit = False
    
        #Create the game clock
        self.clock = pygame.time.Clock()

        self.mm = MoldsManager(self.mold_density, self.mold_velocity)
        self.bm = BottleManager(*levels[self.level]['bottle_density'])
        self.bm.mm = self.mm

        self.total_pos_points = total_pos_points
        self.total_neg_points = total_neg_points

        self.pos_points = 0
        self.neg_points = 0
        
        
        self.pointsCounter = Points(0,0,level=level)
        self.mm.level = self
        self.tics = 0

        self.snow_slim = pygame.sprite.Group()
        self.snow_fat = pygame.sprite.Group()        

        for x in range(75):
            sprite = Wheather(1,2)
            self.snow_slim.add(sprite)

        for x in range(75):
            sprite = Wheather(3,5)
            self.snow_fat.add(sprite)
    
        self.energy_bar = EnergyBar(self.energy_leap)
        self.bm.energy_bar = self.energy_bar

        self.level_time = LevelTime(self.max_time)

        self.gadgets = pygame.sprite.RenderUpdates()
        self.gadgets.add(self.pointsCounter)
        self.gadgets.add(self.energy_bar)
        self.gadgets.add(self.level_time)
    
        #Create the hero parts
        rhand = Part(lit='a', numb=1, top=CENTER, left=0)
        head = Part(lit='b', numb=1, top=CENTER, left=2 * SIDE)
        lhand = Part(lit='c', numb=1, top=CENTER, left=4 * SIDE)
        rarm = Part(lit='d', numb=1, top=CENTER + SIDE, left=0)
        rshould = Part(lit='e', numb=1, top=CENTER + SIDE, left=SIDE)
        cheat = Part(lit='f', numb=1, top=CENTER + SIDE, left=2 * SIDE)
        lshould = Part(lit='g', numb=1, top=CENTER + SIDE, left=3 * SIDE)
        larm = Part(lit='h', numb=1, top=CENTER + SIDE, left=4 * SIDE)
        legs = Part(lit='i', numb=1, top=CENTER + 2 * SIDE, left=2 * SIDE)
        foots = Part(lit='j', numb=1, top=CENTER + 3 * SIDE, left=2 * SIDE)

        parts = dict(rhand=rhand, head=head, lhand=lhand, rarm=rarm, rshould=rshould, \
                            cheat=cheat, lshould=lshould, larm=larm, legs=legs, foots=foots)

        self.hero = Hero(pygame.sprite.RenderUpdates(), parts)
        self.bm.hero=self.hero
        self.mm.hero=self.hero

        self.explotion = Explotion()

        self.control_down = -1
        self.control_up = -1
        self.control_left = -1
        self.control_right = -1
        self.control_tiempo = 5

        #Show level image

        Visual(self.screen, [utils.load_image(levels[self.level]['img'])], [2], None).loop()

    def loop(self):  
        music.play_music(PLAYMUSIC)
        while not self.finish():
            self.tics += 1     
            self.screen.blit(self.background, (-(self.tics % 700),0)) 
            self.update()
            self.draw()

            #Control
            for event in pygame.event.get():
                self.control(event)

            self.clock.tick(CLOCK_TICS)

            if self.control_down == 0: self.hero.down()
            if self.control_up == 0: self.hero.up()
            if self.control_right == 0: self.hero.right()
            if self.control_left == 0: self.hero.left()

            if self.control_down >= 0:
                self.control_down += 1
                if self.control_down >= self.control_tiempo:
                    self.control_down = 0
                    
            if self.control_up >= 0:
                self.control_up += 1
                if self.control_up >= self.control_tiempo:
                    self.control_up = 0

            if self.control_right >= 0:
                self.control_right += 1
                if self.control_right >= self.control_tiempo:
                    self.control_right = 0

            if self.control_left >= 0:
                self.control_left += 1
                if self.control_left >= self.control_tiempo:
                    self.control_left = 0

            self.clock.tick(CLOCK_TICS)

            pygame.display.flip()
    
        if self.exit:
            return self.father
        elif not self.level_time.seconds:        
            if self.pos_points*1.0 / (self.pos_points*1.0 + self.neg_points*1.0) < 0.6:
                def f(screen):
                    def g(screen):
                        return HighScores(self.screen, self.father, self.total_pos_points + self.pos_points) 
                    music.play_gameover()
                    return Visual(screen, [utils.load_image(GAMEOVER)], [3], g)               

                return f
            
            if self.level < LEVELS:
                def f(screen):
                    return Level(screen, self.father, self.level + 1, self.total_pos_points + self.pos_points, self.total_neg_points + self.neg_points)
                return f
            else:
                print self.total_pos_points + self.pos_points #puntos positivos totales
                print self.total_neg_points + self.neg_points #puntos negativos totales
                
                print "definir una funcion que retorne una animacion de victoria"

                def f(screen):
                    return HighScores(self.screen, self.father, self.total_pos_points + self.pos_points)

                return f

        elif self.energy_bar.energy_percent <= 0:
            def f(screen):
                def g(screen):
                    return HighScores(self.screen, self.father, self.total_pos_points + self.pos_points) 
                music.play_gameover()
                return Visual(screen, [utils.load_image(GAMEOVER)], [3], g)               

            return f

    def update(self):
        self.snow_slim.update()
        self.snow_fat.update()        

        self.energy_bar.update(self.tics)
        self.level_time.update(self.tics)

        self.bm.update()        

        self.mm.gen(self.tics)
        self.mm.move(self.tics)
        #Blood Explotion
        self.explotion.update(self.tics, self.screen)
 
        #Verify collision
        if self.mm.fit(self.hero.group, self.tics):
            self.explotion.boom(self.hero.parts['cheat'].rect)
            self.pos_points += 1

        self.pointsCounter.update(self.pos_points, self.neg_points)            
            
    
    def draw(self):
        self.snow_slim.draw(self.screen)
        
        self.bm.draw(self.screen)
        self.mm.draw(self.screen)
        
        self.hero.group.draw(self.screen)
        self.snow_fat.draw(self.screen)    
        self.gadgets.draw(self.screen)

    def control(self, event):
        
        if event.type == QUIT:
            sys.exit(0)

        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                self.control_down = 0
            if event.key == K_UP:
                self.control_up = 0
            if event.key == K_RIGHT:
                self.control_right = 0
            if event.key == K_LEFT:
                self.control_left = 0
            if event.key == K_SPACE:
                self.hero.twist()
                music.play_scream()

            if event.key == K_ESCAPE:
                pygame.mixer.music.set_volume(0.5)
                mem = Menu(self.screen, self.options, "Do you want to quit?").loop()
                pygame.mixer.music.set_volume(1.0)

                if mem == self.father:
                    music.stop_music()
                    self.exit = True

        if event.type == KEYUP:
            if event.key == K_DOWN:
                self.control_down = -1
            if event.key == K_UP:
                self.control_up = -1
            if event.key == K_RIGHT:
                self.control_right = -1
            if event.key == K_LEFT:
                self.control_left = -1

    def finish(self):
        if self.level_time.seconds == 0 or self.energy_bar.energy_percent <= 0 or self.exit:
            return True

        return False


def main():
    Level().loop()

if __name__ == "__main__":
    main()
