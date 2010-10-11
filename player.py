
import random
from ai import SimpleAI
from units import BlueUnit, RedUnit, YellowUnit, GreenUnit

class Player(object):
    def __init__(self, color, dest, bonuses=[20, 50, 100, 200, 500, 1000],
                 spawn=None):
        self.color = color
        self.dest = dest
        self.spawn = spawn
        self.kills = 0
        self.bonuses = bonuses
        self.pad = None
        self.ticks = -1
    def getUnits(self):
        self.ticks += 1
        if self.ticks % 20 == 0:
            units_to_make = self.pad.getUnits()
            return [unit(self, self.spawn.getPoint(), SimpleAI())
                    for unit in units_to_make]
        return []

class LevelPlayer(Player):
    def __init__(self, color, dest):
        super(LevelPlayer, self).__init__(color, dest)
        self.levels = [LevelPlayer.Level(0,    4*[YellowUnit]),
                       LevelPlayer.Level(250,  5*[GreenUnit]),
                       LevelPlayer.Level(500,  7*[BlueUnit]),
                       LevelPlayer.Level(800,  8*[YellowUnit]),
                       LevelPlayer.Level(1100, 9*[RedUnit]),
                       LevelPlayer.Level(1500, 6*[RedUnit]+6*[BlueUnit]),
                       LevelPlayer.Level(1800, 15*[BlueUnit]),
                       LevelPlayer.Level(2100, 5*[GreenUnit]+15*[BlueUnit]),
                       LevelPlayer.Level(2400, 25*[YellowUnit]),
                       LevelPlayer.Level(2700, 15*[RedUnit]+15*[BlueUnit]),
                       LevelPlayer.Level(3000, 30*[YellowUnit]),
                       LevelPlayer.Level(3200, 10*[GreenUnit]),
                       LevelPlayer.Level(2300, 25*[BlueUnit]),
                       ]

    def getUnits(self):
        self.ticks += 1
        if self.levels and self.levels[0].time == self.ticks:
            return [unit(self, self.spawn.getPoint(), SimpleAI())
                    for unit in self.levels.pop(0)]
        return []
            

    class Level(list):
        def __init__(self, time, units):
            super(LevelPlayer.Level, self).__init__(units)
            self.time =  time
