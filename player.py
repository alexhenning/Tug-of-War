
import units, random
from ai import SimpleAI

class Player(object):
    def __init__(self, color, dest, spawn=None):
        self.color = color
        self.dest = dest
        self.spawn = spawn
        self.kills = 0
        self.pad = None
    def getUnit(self, ):
        if self.pad:
            unit = self.pad.getUnit()
        else:
            unit = random.choice([units.BlueUnit, units.RedUnit, units.YellowUnit, units.GreenUnit])
        return unit(self, self.spawn.getPoint(), SimpleAI(self))
