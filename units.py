
import math
from colors import *
from pygame import Rect
from utils import calcAngle, dist
from cmath import sqrt

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
        self.coord = coord
        self.ai = ai
        self.hp = hp
        self.speed = speed

    def move(self, world, dest):
        "Move along the shortest path to the destination"
        if dist(self.rect.center, dest) <= self.speed:
            self.coord = dest
            self.rect.center = dest
        else:
            if dest == self.rect.center: return
            a = dest[0] - self.coord[0]
            b = dest[1] - self.coord[1]
            d = math.sqrt(a**2 + b**2) / self.speed
            self.coord = (self.coord[0] + a/d, self.coord[1] + b/d)
            self.rect.center = self.coord
        
    def act(self, world):
        raise NotImplemented("%s has not implemented act()"%type(self))

    def blit(self, screen):
        raise NotImplemented("%s has not implemented blit()"%type(self))

    def contains(self, p):
        if type(p) == pygame.Rect: return self.rect.contains(p)
        else: return self.rect.contains(pygame.Rect(p[0],p[1], 1, 1))

class SelectionUnit(Unit):
    def __init__(self, player, coord, ai):
        super(SelectionUnit, self).__init__(player, coord, ai, 1000, 4)
        self.dest = self.coord
        self.selected = True

    def act(self, world):
        self.move(world, self.dest)

    def blit(self, screen):
        pygame.draw.circle(screen, self.player.color, self.rect.center, 10)
        pygame.draw.circle(screen, self.getColor(), self.rect.center, 8)
        
    def getColor(self):
        if self.selected: return BLUE
        else: return GRAY
                    
class MilitaryUnit(Unit):
    def __init__(self, player, coord, ai, hp, speed, damage, range_, rate):
        super(MilitaryUnit, self).__init__(player, coord, ai, hp, speed)
        self.damage = damage
        self.range = range_
        self.rate = rate
        
        self.coolOff = 0
        self.firing = False
        self.attackPoint = 0
        
    def act(self, world):
        self.coolOff -= 1
        self.firing = False
        
        action = self.ai.tick(self, world)
        if action.action == "move":
            self.move(world, **action)
        elif action.action == "attack":
            self.attack(world, **action)
            
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

class BlueUnit(MilitaryUnit):
    """ A unit who fights with a "rifle"
    """
    hp = 9; speed = 2; damage = 1.5; distance = 50; rate = 3
    def __init__(self, player, coord, ai):
        super(BlueUnit, self).__init__(player, coord, ai, BlueUnit.hp,
                                       BlueUnit.speed, BlueUnit.damage,
                                       BlueUnit.distance, BlueUnit.rate)

    def blit(self, screen):
        pygame.draw.circle(screen, self.player.color, self.rect.center, 10)
        pygame.draw.circle(screen, self.getColor(), self.rect.center, 8)
        if self.firing:
            pygame.draw.circle(screen, WHITE, self.attackPoint, 2)

    def getColor(self):
        return pygame.Color(int(255 - (255 * self.hp/float(BlueUnit.hp))),
                            int(255 - (255 * self.hp/float(BlueUnit.hp))),
                            255)


class RedUnit(MilitaryUnit):
    """ A unit who fights with a "flame thrower"
    """
    hp = 9; speed = 2; damage = 1.5; distance = 30; rate = 1
    def __init__(self, player, coord, ai):
        super(RedUnit, self).__init__(player, coord, ai, RedUnit.hp,
                                      RedUnit.speed, RedUnit.damage,
                                      RedUnit.distance, RedUnit.rate)

    def blit(self, screen):
        pygame.draw.circle(screen, self.player.color, self.rect.center, 10)
        pygame.draw.circle(screen, self.getColor(), self.rect.center, 8)
        if self.firing:
            p2 = tuple([(self.attackPoint[i]-self.coord[i])*2+self.coord[i]
                        for i in range(2)])
            pygame.draw.circle(screen, RED, self.attackPoint, 4)
            pygame.draw.circle(screen, RED, p2, 8)

    def getColor(self):
        return pygame.Color(255,
                            int(255 - (255 * self.hp/float(RedUnit.hp))),
                            int(255 - (255 * self.hp/float(RedUnit.hp))))
    
class YellowUnit(MilitaryUnit):
    """ A unit who fights with "vicious teeth"
    """
    hp = 13; speed = 3; damage = 4; distance = 25; rate = 3
    def __init__(self, player, coord, ai):
        super(YellowUnit, self).__init__(player, coord, ai, YellowUnit.hp,
                                         YellowUnit.speed, YellowUnit.damage,
                                         YellowUnit.distance,
                                         YellowUnit.rate)

    def blit(self, screen):
        pygame.draw.circle(screen, self.player.color, self.rect.center, 10)
        pygame.draw.circle(screen, self.getColor(), self.rect.center, 8)
        if self.firing:
            pygame.draw.circle(screen, self.player.color, self.attackPoint, 7)
            pygame.draw.circle(screen, self.getColor(), self.attackPoint, 5)

    def getColor(self):
        return pygame.Color(255,
                            255,
                            int(255 - (255 * self.hp/float(YellowUnit.hp))))

class GreenUnit(MilitaryUnit):
    """ A unit who fights with a "sniper rifle"
    """
    hp = 6; speed = 1; damage = 5; distance = 60; rate = 20
    def __init__(self, player, coord, ai):
        super(GreenUnit, self).__init__(player, coord, ai, GreenUnit.hp,
                                        GreenUnit.speed, GreenUnit.damage,
                                        GreenUnit.distance, GreenUnit.rate)

    def blit(self, screen):
        pygame.draw.circle(screen, self.player.color, self.rect.center, 10)
        pygame.draw.circle(screen, self.getColor(), self.rect.center, 8)
        if self.firing:
            pygame.draw.circle(screen, WHITE, self.attackPoint, 4)

    def getColor(self):
        return pygame.Color(int(255 - (255 * self.hp/float(GreenUnit.hp))),
                            126,
                            int(255 - (255 * self.hp/float(GreenUnit.hp))))
