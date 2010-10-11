
import random
from ai import SimpleAI
from units import BlueUnit, RedUnit, YellowUnit, GreenUnit
from colors import BLACK

class Player(object):
    def __init__(self, color, dest, bonuses=[20, 50]+range(100,10000,100),
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

    def blit(self, screen, font):
        pass

class LevelPlayer(Player):
    def __init__(self, color, dest):
        super(LevelPlayer, self).__init__(color, dest)
        self.levels = [LevelPlayer.Level("Lost dogs",
                                         4*[YellowUnit]),
                       LevelPlayer.Level("Wandering snipers",
                                         5*[GreenUnit]),
                       LevelPlayer.Level("Here come the marines",
                                         7*[BlueUnit]),
                       LevelPlayer.Level("And the strange yellow creatures return",
                                         8*[YellowUnit]),
                       LevelPlayer.Level("Pyromaniacs wandering",
                                         9*[RedUnit]),
                       LevelPlayer.Level("Pyromaniacs with friends",
                                         6*[RedUnit]+6*[BlueUnit]),
                       LevelPlayer.Level("More marines",
                                         15*[BlueUnit]),
                       LevelPlayer.Level("Snipers with friends",
                                         5*[GreenUnit]+15*[BlueUnit]),
                       LevelPlayer.Level("Oh, god! The swarm",
                                         25*[YellowUnit]),
                       LevelPlayer.Level("Pyromaniacs with lots of friends",
                                         15*[RedUnit]+15*[BlueUnit]),
                       LevelPlayer.Level("More frakking yellow beasts",
                                         30*[YellowUnit]),
                       LevelPlayer.Level("Hey, this doesn't look so bad",
                                         10*[GreenUnit]),
                       LevelPlayer.Level("Oh... ...",
                                         30*[BlueUnit]),
                       LevelPlayer.Level("Marines with pets",
                                         10*[BlueUnit]+20*[YellowUnit]),
                       LevelPlayer.Level("Pyromaniacs with snipers",
                                         20*[RedUnit]+20*[GreenUnit]),
                       LevelPlayer.Level("And an even scarier swarm",
                                         40*[YellowUnit]),
                       LevelPlayer.Level("Pyromaniacs with pets",
                                         25*[RedUnit]+20*[YellowUnit]),
                       LevelPlayer.Level("A frakking army",
                                         20*[BlueUnit]+30*[RedUnit]),
                       LevelPlayer.Level("The swarm",
                                         60*[YellowUnit]),
                       LevelPlayer.Level("Marines battalion",
                                         70*[BlueUnit]),
                       LevelPlayer.Level("You lose!",
                                         500*[YellowUnit]+500*[RedUnit]+
                                         500*[BlueUnit]+500*[GreenUnit])
                       ]
        self.level = None
        self.levelNum = 0
        self.world = None

    def getUnits(self):
        self.ticks += 1
        if self.levels and len(self.world.p2.units) < 2:
            self.level = self.levels.pop(0)
            self.levelNum += 1
            return [unit(self, self.spawn.getPoint(), SimpleAI())
                    for unit in self.level]
        return []

    def blit(self, screen, font):
        text = font.render("Level %s: %s"%(self.levelNum, self.level.name),
                           True, BLACK)
        screen.blit(text, (400-text.get_width()/2, 446-text.get_height()))

    class Level(list):
        def __init__(self, name, units):
            super(LevelPlayer.Level, self).__init__(units)
            self.name = name
