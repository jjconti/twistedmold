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
levels = {1: dict(energy_leap=0.050, mold_density=70, mold_velocity=35,
                  max_time=20, img=LEVEL1, bottle_density=(300,300,4000,1)),
          2: dict(energy_leap=0.053, mold_density=76, mold_velocity=26,
                  max_time=25, img=LEVEL2, bottle_density=(250,250,3500,3)),
          3: dict(energy_leap=0.057, mold_density=72, mold_velocity=23,
                  max_time=25, img=LEVEL3, bottle_density=(250,200,3200,4)),
          4: dict(energy_leap=0.062, mold_density=67, mold_velocity=18,
                  max_time=30, img=LEVEL4, bottle_density=(200,100,3000,5)),
          5: dict(energy_leap=0.066, mold_density=63, mold_velocity=15,
                  max_time=35, img=LEVEL5, bottle_density=(150,100,2800,7))}

LEVELS = 5

class Level(object):
    '''TwistedMold level'''

    def __init__(self, screen, father, level, total_points):

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

        self.total_points = total_points
        
        self.pointsCounter = Points(self.total_points)
        self.levelIndicator = LevelIndicator(self.level)
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
        self.mm.energy_bar = self.energy_bar

        self.level_time = LevelTime(self.max_time)

        self.gadgets = pygame.sprite.RenderUpdates()
        self.gadgets.add(self.pointsCounter)
        self.gadgets.add(self.energy_bar)
        self.gadgets.add(self.level_time)
        self.gadgets.add(self.levelIndicator)

        self.hero = Hero()
        self.bm.hero=self.hero
        self.mm.hero=self.hero

        self.explotion = Explotion()

        self.control_down = -1
        self.control_up = -1
        self.control_left = -1
        self.control_right = -1
        self.control_tiempo = 5

        self.next_scream = random.randrange(400,500)

        #Show level image
        Visual(self.screen, [utils.load_image(levels[self.level]['img'])], [2], None).loop()

    def loop(self):  
        music.play_music(PLAYMUSIC)
        while not self.finish():
            self.tics += 1  

            if not self.next_scream:
                music.play_random_scream()            
                self.next_scream = random.randrange(400,500)
            else:
                self.next_scream -= 1               
   
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
            music.stop_music()

            if self.level < LEVELS:
                def f(screen):
                    return Level(screen, self.father, self.level + 1, self.total_points)
                return f
            else:
                
                def f(screen):
                    def g(screen):
                        return HighScores(self.screen, self.father, self.total_points)
                    music.play_music(WINMUSIC)
                    return Visual(screen,utils.load_image(WIN),-1,g)
                return f

        elif self.energy_bar.energy_percent <= 0:
            def f(screen):
                def g(screen):
                    return HighScores(self.screen, self.father, self.total_points) 
                music.play_gameover()
                return Visual(screen, [utils.load_image(GAMEOVER)], [3], g)               

            return f

    def update(self):
        if self.level in(3,5):
            self.snow_slim.update()               

        self.energy_bar.update(self.tics)
        self.level_time.update(self.tics)

        self.bm.update()        

        self.mm.gen(self.tics)
        self.mm.move(self.tics)

        if self.level in(3,5):
            self.snow_fat.update() 

        #Blood Explotion
        self.explotion.update(self.tics, self.screen)
 
        #Verify collision
        if self.mm.fit(self.hero, self.tics):
            self.explotion.boom(self.hero.get_center())
            self.total_points += 1

        self.pointsCounter.update(self.total_points)  
        self.levelIndicator.update(self.level)          
            
    
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
            if event.key in(K_SPACE, K_s):
                self.hero.twist_right()
                music.play_scream()
            if event.key == K_a:
                self.hero.twist_left()
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
