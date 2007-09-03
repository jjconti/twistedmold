from config import *

def twist(part, pos=0):
    if pos == 0: _twist_0(part)
    elif pos == 1: _twist_1(part)
    elif pos == 2: _twist_2(part)
    elif pos == 3: _twist_3(part)
    elif pos == 4: _twist_4(part) 
    elif pos == 5: _twist_5(part)

    return (pos + 1) % 6     

def _twist_0(part):
    part['foots'].twist(-side, side, 90)

def _twist_1(part):
    part['lhand'].twist(2 * side, 0, 180)
    part['larm'].twist(0, 0, 0, False, True)

def _twist_2(part):
    part['rhand'].twist(2 * side, 0, 180)
    part['rarm'].twist(0, 0, 0, False, True)

def _twist_3(part):
    part['lhand'].twist(-2 * side, 0, 180)
    part['larm'].twist(0, 0, 0, False, True)
    part['foots'].twist(0, -2 * side, 180)

def _twist_4(part):
    part['foots'].twist(side, side, 90)

def _twist_5(part):
    part['rhand'].twist(-2 * side, 0, 180)
    part['rarm'].twist(0, 0, 0, False, True)

