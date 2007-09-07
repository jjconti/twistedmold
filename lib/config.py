'''In this file are defined values used at the game.'''
import os

WINDOW_TITLE = "Twisted Zombie 1.0"
width = 700
height = 550
center = height / 2

side = 25
half = side / 2


DATA = os.path.join("data")
HISCORES = os.path.join(DATA, "scores.dat")
CREDITS = os.path.join(DATA, "credit.dat")
IMGS = os.path.join(DATA, "imgs")
DROP = os.path.join(IMGS, "drop.gif")
BACKGROUNDS = os.path.join(IMGS, "backgrounds")
INTROS = os.path.join(IMGS, "intro")
parts = os.path.join(IMGS, "body")
SOUNDS = os.path.join(DATA, "sounds")
MUSIC = os.path.join(DATA, "music")
FONTS = os.path.join(DATA, "fonts")

BGIMAGE1 = os.path.join(BACKGROUNDS, "bg1.png")
BGIMAGE2 = os.path.join(BACKGROUNDS, "bg2.png")
MENUBGIMAGE = os.path.join(BACKGROUNDS, "menubg.png")

GAMEOVER = os.path.join(IMGS, "gameover.png")
LEVEL1 = os.path.join(IMGS, "level1.png")
LEVEL2 = os.path.join(IMGS, "level2.png")
LEVEL3 = os.path.join(IMGS, "level3.png")
LEVEL4 = os.path.join(IMGS, "level4.png")


BLOOP = os.path.join(SOUNDS, "bloop.wav")
SCREAM1 = os.path.join(SOUNDS, "31818__malexmedia__malexmedia_man_scream.wav")
SCREAM2 = os.path.join(SOUNDS, "34283__hello_flowers__Flowers_Like_to_Scream_03.wav")
SCREAM3 = os.path.join(SOUNDS, "34292__hello_flowers__Flowers_Like_to_Scream_12.wav")
CRACK1 = os.path.join(SOUNDS, "21914__Halleck__neck_crack.wav")
GAMEOVERMUSIC = os.path.join(SOUNDS, "gameover.ogg")
CREDITSMUSIC = os.path.join(SOUNDS, "credits.ogg")
MENUMUSIC = os.path.join(SOUNDS, "credits.ogg")
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