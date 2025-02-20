import random
import pygame
from circleshape import CircleShape
from constants import * 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 

        angle = random.uniform(20, 50)

        new_vector1 = self.velocity.rotate(angle)
        new_vector2 = self.velocity.rotate(-angle)

        split1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        split2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)

        split1.velocity = new_vector1 * 1.2
        split2.velocity = new_vector2 * 1.2