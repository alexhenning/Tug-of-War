
import pygame

class Color(pygame.Color):
    hashid = 1
    def __init__(self, *args, **kwargs):
        pygame.Color.__init__(self, *args, **kwargs)
        self.hashid = Color.hashid
        Color.hashid += 1
    def __hash__(self):
        return self.hashid

DARKBLUE = Color(0, 0, 126)
DARKRED = Color(126, 0, 0)
BLUE = Color(0, 0, 255)
GRAY = Color(100, 100, 100)
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED  = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 126, 0)

