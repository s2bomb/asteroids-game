import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot



def main():

    print("Start of main")
    
    # intitalise
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (shots, updatables, drawables)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    # game loop
    while True:
       
        # escape to close
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return

        # allows window closes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # UPDATE
        updatables.update(dt)
        
        # check_collisions
        for asteroid in asteroids:
            if asteroid.has_collided(player):
                print("Game over!")
                return

        for asteroid in asteroids:
            for shot in shots:
                if shot.has_collided(asteroid):
                    shot.kill()
                    asteroid.split()
                    print("booom")

        # RENDER -------
        # create black screen
        screen.fill(pygame.Color(0, 0, 0))

        # DRAW
        for drawable in drawables:
            drawable.draw(screen)
        
        # refresh the screen
        pygame.display.flip()
        # RENDER -------

        # pause the game loop until the 1/60th second has passed
        clock.tick(60)
        dt = clock.tick(60) / 1000
        # print(dt)


if __name__ == "__main__":
    main()
