
from colors import *

class Unit(object):
    """ The base class for units
    """
    
    def __init__(self, player, coord, ai):
        """
        Arguments:
        - `player`: The player that this unit fights for.
        - `coord`: The coordinates of the unit.
        - `ai`: An AI object to control the unit.
        """
        self.player = player
        self.coord = coord
        self.ai = ai

class BlueUnit(Unit):
    """ A unit who fights with a "rifle"
    """
    
    def __init__(self, player, coord, ai):
        super(BlueUnit, self).__init__(player, coord, ai)

    def blit(self, screen):
        pygame.draw.circle(screen, self.player, self.coord, 10)
        pygame.draw.circle(screen, BLUE, self.coord, 8)
