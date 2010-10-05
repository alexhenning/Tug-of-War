
import random, math
from utils import dist

class Action(dict):
    def __init__(self, action, **kwargs):
        self.action = action
        super(Action, self).__init__(**kwargs)

class SimpleAI(object):
    def __init__(self, player):
        self.player = player
    def tick(self, me, world):
        enemies = [unit for unit in world.units if unit.player != self.player]

        closest, _dist = None, 1000
        for enemy in enemies:
            d = dist(me, enemy)
            if d < _dist:
                closest, _dist = enemy, d

        if _dist <= me.range and me.coolOff <= 0:
            return Action("attack", unit=closest)
        elif closest:
            return Action("move", dest=closest.rect.center)
        else:
            return Action("move", dest=self.player.dest)
