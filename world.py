
import pygame, random, units

from colors import *

class World(object):
    def __init__(self):
        """ An object that represents the world
        """

        self.ticks = 0

        self.blueSpawn = Rect(0, 25, 50, 200, DARKBLUE)
        
        self.objects = [self.blueSpawn,
                        Rect(50, 25, 700, 200, GRAY),
                        Rect(750, 25, 50, 200, DARKRED)]

        self.units = []
        
    def tick(self):
        self.ticks += 1

        if self.ticks % 20 == 0:
            self.units.append(units.BlueUnit(DARKBLUE, self.blueSpawn.getPoint(), ()))
            
            
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
