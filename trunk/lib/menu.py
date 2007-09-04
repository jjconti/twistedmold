import pygame
import os
from runmenu import Menu
from pygame.locals import *

#Colours

color1 = (0, 255, 5)
color2 = (0, 5 , 0)
color5 = (0, 255, 0)

black = (0,0,0)
white = (255, 255, 255)

def load_image(fullname, colorkey=None):

    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

def history():
	print "hola..esta es la historia"

def main():
	pygame.init()
	DATA = os.path.join('..',"data")
	FONTS = os.path.join(DATA, "fonts")
	FONT1 = os.path.join(FONTS,"tasapainoaisti.ttf")
	FONT2 = os.path.join(FONTS, "attic.ttf")
	font0 = pygame.font.Font(FONT1, 65)
	font1 = pygame.font.Font(FONT1, 50)
	font2 = pygame.font.Font(FONT1, 65)
	font3 = pygame.font.Font(FONT1, 50)
	font4 = pygame.font.Font(FONT1, 50)
	#sound1 = load_sound(TYPEW1)
	#sound2 = load_sound(TYPEW2)

	screen = pygame.display.set_mode((700,550))
	IMGS = os.path.join(DATA, "imgs")
	
	BACKGROUNDS = os.path.join(IMGS, "backgrounds")
	BGIMAGE1 = os.path.join(BACKGROUNDS, "paper3.png")
	background = load_image(BGIMAGE1)
	pygame.display.set_caption('TWISTED MOLDS')
	background = load_image(BGIMAGE1)
	title="MAIN MENU"
	options = [("Start Play", None),
                ("History", history),
                ("Setup", None),
                ("Help", None),
                ("Quit",  None),]

	men = Menu(screen, background, font3, font4, font0, color1, color2, color5, \
        None, None, title, options)
	return men.main_loop()
	
if __name__ == '__main__':
    main()
