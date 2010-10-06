
import pygame, sys
from world import World
from player import Player
from colors import *

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800, 450))
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((180, 180, 180))
    f = pygame.font.Font(pygame.font.get_default_font(), 20)

    w = World(Player(DARKBLUE, (800, 125)), Player(DARKRED, (0, 125)))

    clock = pygame.time.Clock()

    contin = True
    while contin or True:
        for event in pygame.event.get():
            if event.type == pygame.constants.QUIT: sys.exit(0)
            elif event.type == pygame.constants.MOUSEBUTTONUP:
                if event.button == 1: w.leftClick(event.pos)
                elif event.button == 3: w.rightClick(event.pos)
                else: print event

        w.tick()
            
        screen.blit(background, (0, 0))
        contin = w.blit(screen, f)
        pygame.display.flip()
        
        clock.tick(20)

if __name__ == "__main__":
    main()
