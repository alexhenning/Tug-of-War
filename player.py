
import units, random
from ai import SimpleAI

class Player(object):
    def __init__(self, color, dest, bonuses=[20, 50, 100, 200, 500, 1000],
                 spawn=None):
        self.color = color
        self.dest = dest
        self.spawn = spawn
        self.kills = 0
        self.bonuses = bonuses
        self.pad = None
    def getUnits(self):
        units_to_make = self.pad.getUnits()
        return [unit(self, self.spawn.getPoint(), SimpleAI())
                for unit in units_to_make]
