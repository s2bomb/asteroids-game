import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
       
        # allows window closes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # create black screen
        screen.fill(pygame.Color(0, 0, 0))

        pygame.display.flip()



if __name__ == "__main__":
    main()
