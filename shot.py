from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS


class Shot(CircleShape):
    
    containers = tuple()

    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)
        

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
