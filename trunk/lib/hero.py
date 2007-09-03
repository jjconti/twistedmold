from config import *
from twist import twist

class Hero():

    def __init__(self, group, parts):
        self.group = group
        self.group.add(parts.values())
        self.parts = parts
        self.pos = 0
    
    def up(self):
        top = min([p.rect.top for p in self.group])
        if top > 0:
            for p in self.group:
                p.up()

    def down(self):
        bottom = max([p.rect.bottom for p in self.group])
        if bottom < height:
            for p in self.group:
                p.down()

    def left(self):
        left = min([p.rect.left for p in self.group])
        if left > 0:
            for p in self.group:
                p.left()

    def right(self):
        right = max([p.rect.right for p in self.group])
        if right < width:
            for p in self.group:
                p.right()

    def twist(self):
        self.pos = twist(self.parts, self.pos)

