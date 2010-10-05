
import pygame, sys
from world import World
from player import Player
from colors import *

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800, 600))
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    f = pygame.font.Font(pygame.font.get_default_font(), 20)

    w = World(Player(DARKBLUE, (800, 50)), Player(DARKRED, ()))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.constants.QUIT: sys.exit(0)

        w.tick()
            
        screen.blit(background, (0, 0))
        w.blit(screen)
        pygame.display.flip()
        
        clock.tick(20)

if __name__ == "__main__":
    main()
