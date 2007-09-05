'''In this file are defined values used at the game.'''
import os

WINDOW_TITLE = "Twisted Zombies 1.0"
width = 700
height = 550
center = height / 2

side = 25
half = side / 2


DATA = os.path.join("data")
HISCORES = os.path.join(DATA, "scores.high")
IMGS = os.path.join(DATA, "imgs")
DROP = os.path.join(IMGS, "gota.gif")
BACKGROUNDS = os.path.join(IMGS, "backgrounds")
parts = os.path.join(IMGS, "body")
SOUNDS = os.path.join(DATA, "sounds")
MUSIC = os.path.join(DATA, "music")
FONTS = os.path.join(DATA, "fonts")

BGIMAGE1 = os.path.join(BACKGROUNDS, "bg1.png")

BLOOP = os.path.join(SOUNDS, "bloop.wav")
SCREAM1 = os.path.join(SOUNDS, "31818__malexmedia__malexmedia_man_scream.wav")
SCREAM2 = os.path.join(SOUNDS, "34283__hello_flowers__Flowers_Like_to_Scream_03.wav")
SCREAM3 = os.path.join(SOUNDS, "34292__hello_flowers__Flowers_Like_to_Scream_12.wav")

                     
#FONT1 = os.path.join(FONTS,"FreeMonoBold.ttf")
#FONT1 = os.path.join(FONTS,"ds_moster.ttf")
FONT1 = os.path.join(FONTS, "FreeSerifBold.ttf")


COLOR1 = (10, 50, 200) 
BLACK = (0, 0, 0)
GREEN = (0,250,0)
ORANGE = (255, 180, 0)
RED = (250, 0, 0)
WHITE = (250, 250, 250)
GREY = (200, 200, 200)
