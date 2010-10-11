
import random
from utils import dist

class Action(dict):
    def __init__(self, action, **kwargs):
        self.action = action
        super(Action, self).__init__(**kwargs)

class SimpleAI(object):
    def tick(self, me, world):
        if me.player == world.p1: enemies = world.p2.units
        else: enemies = world.p1.units
        # enemies = [unit for unit in world.units if unit.player != self.player]

        closest, _dist = None, 1000
        for enemy in enemies[:100]:
            d = abs(me.rect.x - enemy.rect.x) + abs(me.rect.y - enemy.rect.y)
            if d < _dist:
                closest, _dist = enemy, d

        if closest and dist(me.rect, closest.rect) <= me.range \
                and me.coolOff <= 0:
            return Action("attack", unit=closest)
#        elif closest and dist(me.rect, closest.rect) <= me.range:
#            return Action("wait")
        elif closest:
            return Action("move", dest=closest.rect.center)
        else:
            return Action("move", dest=me.player.dest)
