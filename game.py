
import pygame, sys

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800, 600))
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    f = pygame.font.Font(pygame.font.get_default_font(), 20)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.constants.QUIT: sys.exit(0)

        screen.blit(background, (0, 0))
            
        pygame.display.flip()
        
        clock.tick(20)

if __name__ == "__main__":
    main()