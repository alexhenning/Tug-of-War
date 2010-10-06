
import math
from colors import *
from pygame import Rect
from utils import calcAngle

class Unit(object):
    def __init__(self, player, coord, ai, hp, speed):
        """
        Arguments:
        - `player`: The player that this unit fights for.
        - `coord`: The coordinates of the unit.
        - `ai`: An AI object to control the unit.
        """
        self.player = player
        self.rect = Rect(coord[0]-5, coord[1]-5, 10, 10)
        self.ai = ai
        self.hp = hp
        self.speed = speed

    def act(self, world):
        raise NotImplemented("%s has not implemented act()"%type(self))

class SelectionUnit(Unit):
    def __init__(self, player, coord, ai, bounds):
        super(SelectionUnit, self).__init__(player, coord, ai, 1000, 4)
        self.bounds = bounds
    
class MilitaryUnit(Unit):
    def __init__(self, player, coord, ai, hp, speed, damage, range_, rate):
        super(MilitaryUnit, self).__init__(player, coord, ai, hp, speed)
        self.damage = damage
        self.range = range_
        self.rate = rate
        
        self.coolOff = 0
        self.firing = False
        self.coord = self.rect.center
        self.attackPoint = 0
        
    def act(self, world):
        self.coolOff -= 1
        self.firing = self.isFiring()
        
        action = self.ai.tick(self, world)
        if action.action == "move":
            self.move(world, **action)
        elif action.action == "attack":
            self.attack(world, **action)
            
    def move(self, world, dest):
        "Move along the shortest path to the destination"
        if dest == self.rect.center: return
        a = dest[0] - self.coord[0]
        b = dest[1] - self.coord[1]
        c = math.sqrt(a**2 + b**2)
        d = c / self.speed
        self.coord = (self.coord[0] + a/d, self.coord[1] + b/d)
        self.rect.center = self.coord
        
    def attack(self, world, unit):
        "Attack the unit"
        self.coolOff = self.rate
        self.firing = True
        self.setAttackPoint(unit)
        unit.sufferDamage(self.damage, world)

    def sufferDamage(self, damage, world=None):
        self.hp -= damage
        if self.hp <= 0 and world:
            world.kill(self)

    def setAttackPoint(self, unit):
        attackAngle = calcAngle(self.coord, unit.coord)
        self.attackPoint = (self.coord[0] - 10*math.cos(attackAngle),
                            self.coord[1] - 10*math.sin(attackAngle))
    def isFiring(self): return False

class BlueUnit(MilitaryUnit):
    """ A unit who fights with a "rifle"
    """
    def __init__(self, player, coord, ai):
        super(BlueUnit, self).__init__(player, coord, ai, 10, 2, 1, 40, 2)

    def blit(self, screen):
        pygame.draw.circle(screen, self.player.color, self.rect.center, 10)
        pygame.draw.circle(screen, self.getColor(), self.rect.center, 8)
        if self.firing:
            pygame.draw.circle(screen, WHITE, self.attackPoint, 2)

    def getColor(self):
        return pygame.Color(int(255 - (255 * self.hp/10.)),
                            int(255 - (255 * self.hp/10.)),
                            255)


class RedUnit(MilitaryUnit):
    """ A unit who fights with a "flame thrower"
    """
    def __init__(self, player, coord, ai):
        super(RedUnit, self).__init__(player, coord, ai, 20, 2, 5, 30, 4)

    def blit(self, screen):
        pygame.draw.circle(screen, self.player.color, self.rect.center, 10)
        pygame.draw.circle(screen, self.getColor(), self.rect.center, 8)
        if self.firing:
            p2 = tuple([(self.attackPoint[i]-self.coord[i])*2+self.coord[i]
                        for i in range(2)])
            pygame.draw.circle(screen, RED, self.attackPoint, 4)
            pygame.draw.circle(screen, RED, p2, 8)

    def isFiring(self): return self.coolOff > self.rate-3

    def getColor(self):
        return pygame.Color(255,
                            int(255 - (255 * self.hp/20.)),
                            int(255 - (255 * self.hp/20.)))
    
class YellowUnit(MilitaryUnit):
    """ A unit who fights with "vicious teeth"
    """
    def __init__(self, player, coord, ai):
        super(YellowUnit, self).__init__(player, coord, ai, 8, 3, 1, 20, 1)

    def blit(self, screen):
        pygame.draw.circle(screen, self.player.color, self.rect.center, 10)
        pygame.draw.circle(screen, self.getColor(), self.rect.center, 8)
        if self.firing:
            pygame.draw.circle(screen, self.player.color, self.attackPoint, 7)
            pygame.draw.circle(screen, self.getColor(), self.attackPoint, 5)

    def getColor(self):
        return pygame.Color(255,
                            255,
                            int(255 - (255 * self.hp/8.)))

class GreenUnit(MilitaryUnit):
    """ A unit who fights with a "sniper rifle"
    """
    def __init__(self, player, coord, ai):
        super(GreenUnit, self).__init__(player, coord, ai, 5, 1, 25, 60, 40)

    def blit(self, screen):
        pygame.draw.circle(screen, self.player.color, self.rect.center, 10)
        pygame.draw.circle(screen, self.getColor(), self.rect.center, 8)
        if self.firing:
            pygame.draw.circle(screen, WHITE, self.attackPoint, 4)

    def getColor(self):
        return pygame.Color(int(255 - (255 * self.hp/5.)),
                            126,
                            int(255 - (255 * self.hp/5.)))
