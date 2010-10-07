
import pygame, random, units
from colors import BLUE, GREEN, GRAY, RED, YELLOW, BLACK

class World(object):
    def __init__(self, p1, p2):
        """ An object that represents the world
        """

        self.ticks = 0

        self.p1 = p1
        self.p1.spawn = Rect(0, 25, 50, 200, self.p1.color)
        self.p1.pad = Pad(0, 275, self.p1)
        self.p1.units = []

        self.p2 = p2
        self.p2.spawn = Rect(750, 25, 50, 200, self.p2.color)
        self.p2.pad = Pad(650, 275, self.p2)
        self.p2.units = []
        
        self.objects = [self.p1.spawn,
                        self.p1.pad,
                        Rect(50, 25, 700, 200, GRAY),
                        self.p2.spawn,
                        self.p2.pad]

        self.units = []
                                 
    def tick(self):
        self.ticks += 1

        if self.ticks % 20 == 0:
            for unit in self.p2.getUnits():
                self.p2.units.append(unit)
                self.units.append(unit)
            for unit in self.p1.getUnits():
                self.p1.units.append(unit)
                self.units.append(unit)
            
        for unit in self.units:
            unit.act(self)

        self.p1.pad.tick(self)
        self.p2.pad.tick(self)
            
        for unit in self.units:
            if unit.player == self.p1:
                if self.p2.spawn.contains(unit.rect):
                    return False
            else:
                if self.p1.spawn.contains(unit.rect):
                    return False
        return True
            
    def blit(self, screen, font):
        for i in self.objects:
            i.blit(screen)
        for unit in self.units:
            unit.blit(screen)
        temp = "%s - kills: %s units: %s"
        s = temp%("Blue", self.p1.kills, len([i for i in self.units
                                              if i.player == self.p1]))
        screen.blit(font.render(s, True, BLACK), (5, 4))
        
        s = temp%("Red", self.p2.kills, len([i for i in self.units
                                              if i.player == self.p2]))
        text = font.render(s, True, BLACK)
        screen.blit(text, (795-text.get_width(), 4))


    def kill(self, unit):
        self.units.remove(unit)
        if unit.player == self.p1:
            self.p1.units.remove(unit)
            self.p2.kills +=1
            if self.p2.kills in self.p2.bonuses:
                self.p2.pad.addUnit()
        else:
            self.p2.units.remove(unit)
            self.p1.kills += 1
            if self.p1.kills in self.p1.bonuses:
                self.p1.pad.addUnit()

    def leftClick(self, pos):
        if self.p1.pad.contains(pygame.Rect(pos[0], pos[1], 1, 1)):
            self.p1.pad.leftClick(pos)
        if self.p2.pad.contains(pygame.Rect(pos[0], pos[1], 1, 1)):
            self.p2.pad.leftClick(pos)

    def rightClick(self, pos):
        if self.p1.pad.contains(pygame.Rect(pos[0], pos[1], 1, 1)):
            self.p1.pad.rightClick(pos)
        if self.p2.pad.contains(pygame.Rect(pos[0], pos[1], 1, 1)):
            self.p2.pad.rightClick(pos)

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
                self.units[self.selected].selected = False
                self.selected = self.units.index(unit)
                self.units[self.selected].selected = True

    def rightClick(self, pos):
        self.units[self.selected].dest = pos

    def addUnit(self):
        self.units[self.selected].selected = False
        self.units.append(units.SelectionUnit(self.player, (self.parts[2].rect.x+25,
                                                            self.parts[2].rect.y+25),
                                              ()))
        self.selected = len(self.units)-1
        
    def getUnits(self):
        units = []
        for unit in self.units:
            for part in self.parts:
                if part.contains(unit.rect):
                    units.append(unitMap[part.color]())
        return units
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
