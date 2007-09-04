'''In this file are defined values used at the game.'''
import os

WINDOW_TITLE = "Twisted Zombies 1.0"
width = 700
height = 550
center = height / 2

side = 25
half = side / 2
parts = os.path.join("data")


DATA = os.path.join("data")
HISCORES = os.path.join(DATA, "scores.high")
IMGS = os.path.join(DATA, "imgs")
BACKGROUNDS = os.path.join(IMGS, "backgrounds")
SOUNDS = os.path.join(DATA, "sounds")
MUSIC = os.path.join(DATA, "music")
FONTS = os.path.join(DATA, "fonts")

BGIMAGE1 = os.path.join(BACKGROUNDS, "paper3.png")
PLAY = os.path.join(IMGS, "play.png")
STOP = os.path.join(IMGS, "stop.png")
NEXT = os.path.join(IMGS, "next.png")
PREV = os.path.join(IMGS, "prev.png")

BLOOP = os.path.join(SOUNDS, "bloop.wav")
TYPEW1 = os.path.join(SOUNDS, "9744_Horn_typewriter-shorter.wav")
TYPEW2 = os.path.join(SOUNDS, "9098_ddohler_Typewriter.wav")

                      
#FONT1 = os.path.join(FONTS,"FreeMonoBold.ttf")
FONT1 = os.path.join(FONTS,"ds_moster.ttf")
FONT2 = os.path.join(FONTS, "FreeSerifBold.ttf")

MOVE_TICK = 20
