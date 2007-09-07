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


last_music = False

def play_menu1():
    SOUNDS['sword1'].play()

def play_menu2():
    SOUNDS['sword2'].play()

def play_bloop():
    SOUNDS['eat'].play()

def play_scream():
    SOUNDS['crack1'].play()

def play_gameover():
    SOUNDS['gameover'].play()

def play_music(music_name):
    global last_music
    if last_music != music_name:
        last_music = music_name
        pygame.mixer.music.load(music_name)
        pygame.mixer.music.play(-1)

def stop_music():
    global last_music
    last_music = False
    pygame.mixer.music.stop()
