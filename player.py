
import units, random
from ai import SimpleAI

class Player(object):
    def __init__(self, color, dest, spawn=None):
        self.color = color
        self.dest = dest
        self.spawn = spawn
    def getUnit(self, ):
        unit = random.choice([units.BlueUnit, units.RedUnit, units.YellowUnit, units.GreenUnit])
        return unit(self, self.spawn.getPoint(), SimpleAI(self))
