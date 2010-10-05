
import math
from colors import *

class Unit(object):
    def __init__(self, player, coord, ai, hp, speed):
        """
        Arguments:
        - `player`: The player that this unit fights for.
        - `coord`: The coordinates of the unit.
        - `ai`: An AI object to control the unit.
        """
        self.player = player
        self.coord = coord
        self.ai = ai
        self.hp = hp
        self.speed = speed

    def act(self, world):
        raise NotImplemented("%s has not implemented act()"%type(self))

class MilitaryUnit(Unit):
    def __init__(self, player, coord, ai, hp, speed, damage, range_, rate):
        super(MilitaryUnit, self).__init__(player, coord, ai, hp, speed)
        self.damage = damage
        self.range = range_
        self.rate = rate
    def act(self, world):
        action = self.ai.tick(world)
        if action.action == "move":
            self.move(**action)
        elif action.action == "attack":
            self.attact**action)
    def move(self, dest):
        "Move along the shortest path to the destination"
        a = dest[0] - self.coord[0]
        b = dest[1] - self.coord[1]
        c = math.sqrt(a**2 + b**2)
        d = c / self.speed
        self.coord = (self.coord[0] + a/d, self.coord[1] + b/d)
    def attack(self, unit):
        "Attack the unit"

        
class BlueUnit(MilitaryUnit):
    """ A unit who fights with a "rifle"
    """
    def __init__(self, player, coord, ai):
        super(BlueUnit, self).__init__(player, coord, ai, 10, 2, 1, 2, 10)

    def blit(self, screen):
        pygame.draw.circle(screen, self.player.color, self.coord, 10)
        pygame.draw.circle(screen, BLUE, self.coord, 8)
