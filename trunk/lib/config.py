'''In this file are defined values used at the game.'''
import os

WINDOW_TITLE = "Twisted Zombie 1.0"
WIDTH = 700
HEIGHT = 550
CENTER = HEIGHT / 2

SIDE = 25
HALF = SIDE / 2

LEVEL_TOP = 1
LEVEL_LEFT = 0
LEVEL_WIDTH = WIDTH / SIDE - LEVEL_LEFT
LEVEL_HEIGHT = HEIGHT / SIDE - LEVEL_TOP

DATA = os.path.join("data")
HISCORES = os.path.join(DATA, "scores.dat")
CREDITS = os.path.join(DATA, "credits.txt")
IMGS = os.path.join(DATA, "imgs")
DROP = os.path.join(IMGS, "drop.gif")
BACKGROUNDS = os.path.join(IMGS, "backgrounds")
INTROS = os.path.join(IMGS, "intro")
BOTTLES = os.path.join(IMGS, "bottles")
PARTS = os.path.join(IMGS, "body")
SOUNDS = os.path.join(DATA, "sounds")
MUSIC = os.path.join(DATA, "music")
FONTS = os.path.join(DATA, "fonts")

ICON = os.path.join(IMGS, "icon.jpg")
BGIMAGE1 = os.path.join(BACKGROUNDS, "bg1.png")
BGIMAGE2 = os.path.join(BACKGROUNDS, "bg2.png")
MENUBGIMAGE = os.path.join(BACKGROUNDS, "menubg.png")
CREDITIMAGE = os.path.join(IMGS, "cemetery-moon.png")
GAMEOVER = os.path.join(IMGS, "gameover.png")
LEVEL1 = os.path.join(IMGS, "level1.png")
LEVEL2 = os.path.join(IMGS, "level2.png")
LEVEL3 = os.path.join(IMGS, "level3.png")
LEVEL4 = os.path.join(IMGS, "level4.png")
STORY = os.path.join(IMGS, "story.png")
STORYBG = os.path.join(IMGS, "for-story.png")
HELP = os.path.join(IMGS, "help.png") # Reemplazar por un texto con la ayuda.
HELPBG = os.path.join(IMGS, "horror-house.png")

BLOOP = os.path.join(SOUNDS, "bloop.wav")
SWORD1 = os.path.join(SOUNDS, "37596__hello_flowers__Sword.wav")
SWORD2 = os.path.join(SOUNDS, "29613__Erdie__Rubbing_metal03.wav")
SCREAM1 = os.path.join(SOUNDS, "31818__malexmedia__malexmedia_man_scream.wav")
SCREAM2 = os.path.join(SOUNDS, "34283__hello_flowers__Flowers_Like_to_Scream_03.wav")
SCREAM3 = os.path.join(SOUNDS, "34292__hello_flowers__Flowers_Like_to_Scream_12.wav")
CRACK1 = os.path.join(SOUNDS, "21914__Halleck__neck_crack.wav")
GAMEOVERMUSIC = os.path.join(SOUNDS, "gameover.ogg")
CREDITSMUSIC = os.path.join(SOUNDS, "credits.ogg")
MENUMUSIC = os.path.join(SOUNDS, "menu.ogg")
PLAYMUSIC = os.path.join(SOUNDS, "credits.ogg")
                     
FONT1 = os.path.join(FONTS, "FreeSerifBold.ttf")
FONT2 = os.path.join(FONTS, "tasapainoaisti.ttf")
FONT3 = os.path.join(FONTS, "acquaint.ttf")

COLOR1 = (10, 50, 200) 
BLACK = (0, 0, 0)
GREEN = (0,250,0)
ORANGE = (255, 180, 0)
RED = (250, 0, 0)
WHITE = (250, 250, 250)
GREY = (100, 100, 100)

CLOCK_TICS = 80

# imagenes intro
INTRO_IMAGES = [os.path.join(INTROS, "intro0001.png"),
                os.path.join(INTROS, "intro0009.png"),
                os.path.join(INTROS, "intro0015.png"),
                os.path.join(INTROS, "intro0016.png"),
                os.path.join(INTROS, "intro0017.png"),
                os.path.join(INTROS, "intro0018.png"),
                os.path.join(INTROS, "intro0019.png"),
                os.path.join(INTROS, "intro0020.png"),
                os.path.join(INTROS, "intro0021.png"),
                os.path.join(INTROS, "intro0022.png"),
                os.path.join(INTROS, "intro0023.png"),
                os.path.join(INTROS, "intro0024.png"),
                os.path.join(INTROS, "intro0025.png"),
                os.path.join(INTROS, "intro0032.png"),
                os.path.join(INTROS, "intro0033.png"),
                os.path.join(INTROS, "intro0034.png"),
                os.path.join(INTROS, "intro0035.png"),
                ]

INTRO_TIMES = [0.672, 0.504, 0.084, 0.084, 0.084, 0.084, 0.084, 0.084, 0.084,
               0.084, 0.084, 0.084, 0.588, 0.084, 0.084, 0.084, 2.856]

BOTTLE_BLUE = os.path.join(BOTTLES, "bottle_blue.png")
BOTTLE_GREEN = os.path.join(BOTTLES, "bottle_green.png")
BOTTLE_ORANGE  = os.path.join(BOTTLES, "bottle_orange.png")
BOTTLE_RED  = os.path.join(BOTTLES, "bottle_red.png")

BODY1 = os.path.join(IMGS, os.path.join("body", "body1.png"))
