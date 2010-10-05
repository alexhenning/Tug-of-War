
import pygame, random, units
from ai import SimpleAI
from colors import *

class World(object):
    def __init__(self, p1, p2):
        """ An object that represents the world
        """

        self.ticks = 0

        self.p1 = p1
        self.p1Spawn = Rect(0, 25, 50, 200, self.p1.color)

        self.p2 = p2
        
        self.objects = [self.p1Spawn,
                        Rect(50, 25, 700, 200, GRAY),
                        Rect(750, 25, 50, 200, DARKRED)]

        self.units = []
        
    def tick(self):
        self.ticks += 1

        if self.ticks % 20 == 0:
            self.units.append(units.BlueUnit(self.p1,
                                             self.p1Spawn.getPoint(),
                                             SimpleAI(self.p1)))
        for unit in self.units:
            unit.act(self)
            
    def blit(self, screen):
        for i in self.objects:
            i.blit(screen)
        for unit in self.units:
            unit.blit(screen)

class Rect(object):
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    def blit(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    def getPoint(self):
        return (random.randint(self.rect.x, self.rect.width) + self.rect.x,
                random.randint(self.rect.y, self.rect.height) + self.rect.y)
