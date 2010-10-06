
import pygame, random, units
from colors import BLUE, GREEN, GRAY, RED, YELLOW

class World(object):
    def __init__(self, p1, p2):
        """ An object that represents the world
        """

        self.ticks = 0

        self.p1 = p1
        self.p1.spawn = Rect(0, 25, 50, 200, self.p1.color)
        self.p1.pad = Pad(0, 275, self.p1)

        self.p2 = p2
        self.p2.spawn = Rect(750, 25, 50, 200, self.p2.color)
        self.p2pad = Pad(650, 275, self.p2)
        
        self.objects = [self.p1.spawn,
                        self.p1.pad,
                        Rect(50, 25, 700, 200, GRAY),
                        self.p2.spawn,
                        self.p2pad]

        self.units = []
                                 
    def tick(self):
        self.ticks += 1

        if self.ticks % 20 == 0:
            self.units.append(self.p1.getUnit())
            self.units.append(self.p2.getUnit())
            
        for unit in self.units:
            unit.act(self)

        self.p1.pad.tick(self)
            
        for unit in self.units:
            if unit.player == self.p1:
                if self.p2.spawn.contains(unit.rect):
                    return False
            else:
                if self.p1.spawn.contains(unit.rect):
                    return False
        return True
            
    def blit(self, screen):
        for i in self.objects:
            i.blit(screen)
        for unit in self.units:
            unit.blit(screen)

    def kill(self, unit):
        self.units.remove(unit)

    def leftClick(self, pos):
        if self.p1.pad.contains(pygame.Rect(pos[0], pos[1], 1, 1)):
            self.p1.pad.leftClick(pos)

    def rightClick(self, pos):
        if self.p1.pad.contains(pygame.Rect(pos[0], pos[1], 1, 1)):
            self.p1.pad.rightClick(pos)

class Pad(object):
    def __init__(self, x, y, player):
        self.parts = [Rect(x+50, y, 50, 50, BLUE),
                      Rect(x, y+50, 50, 50, GREEN),
                      Rect(x+50, y+50, 50, 50, GRAY),
                      Rect(x+100, y+50, 50, 50, RED),
                      Rect(x+50, y+100, 50, 50, YELLOW)]
        self.player = player
        self.units = [units.SelectionUnit(self.player, (x+75, y+75), ())]
        self.selected = 0

    def tick(self, world):
        for unit in self.units:
            unit.act(world)
        
    def blit(self, screen):
        for part in self.parts:
            part.blit(screen)
        for unit in self.units:
            unit.blit(screen)
            
    def contains(self, rect):
        for i in self.parts:
            if i.contains(rect):
                return True
        return False

    def leftClick(self, pos):
        for unit in self.units:
            if unit.contains(pos):
                self.selected = self.units.index(unit)

    def rightClick(self, pos):
        self.units[self.selected].dest = pos

    def getUnit(self):
        for part in self.parts:
            if part.contains(self.units[0].rect):
                return unitMap[part.color]()
unitMap = {BLUE: lambda: units.BlueUnit,
           RED: lambda: units.RedUnit,
           YELLOW: lambda: units.YellowUnit,
           GREEN: lambda: units.GreenUnit,
           GRAY: lambda: random.choice([units.BlueUnit, units.RedUnit, units.YellowUnit, units.GreenUnit])}
        
class Rect(object):
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.contains = lambda x: self.rect.contains(x)
    def blit(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    def getPoint(self):
        x, y, w, h = self.rect.x, self.rect.y, self.rect.width, self.rect.height
        return (random.randint(x, x+w),
                random.randint(y, y+h))
