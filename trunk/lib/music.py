from config import *
import utils

SOUNDS = {}
SOUNDS['eat'] = utils.load_sound(BLOOP)

def play_bloop():
    SOUNDS['eat'].play()
