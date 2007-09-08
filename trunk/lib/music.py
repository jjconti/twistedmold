import random
from config import *
import utils
import pygame
pygame.init()
pygame.mixer.init()

SOUNDS = {}
SOUNDS['eat'] = utils.load_sound(BLOOP)
SOUNDS['scream1'] = utils.load_sound(SCREAM1)
SOUNDS['scream2'] = utils.load_sound(SCREAM2)
SOUNDS['scream3'] = utils.load_sound(SCREAM3)
SOUNDS['crack1'] = utils.load_sound(CRACK1)
SOUNDS['gameover'] = utils.load_sound(GAMEOVERMUSIC)
SOUNDS['sword1'] = utils.load_sound(SWORD1)
SOUNDS['sword2'] = utils.load_sound(SWORD2)
SOUNDS['play_music'] = utils.load_sound(PLAYMUSIC)

last_music = None

def play_menu1():
    SOUNDS['sword1'].set_volume(0.5)
    SOUNDS['sword1'].play()

def play_menu2():
    SOUNDS['sword2'].set_volume(0.5)
    SOUNDS['sword2'].play()

def play_bloop():
    SOUNDS['eat'].play()

def play_scream():
    SOUNDS['crack1'].play()

def play_random_scream():
    SOUNDS['scream1'].play()

def play_gameover():
    SOUNDS['gameover'].play()

def play_music(level):
    SOUNDS['play_music'].play()    

def stop_music():
    global last_music
    last_music = None
    pygame.mixer.music.stop()

def is_playing_music():
    return last_music != None
