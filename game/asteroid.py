from .circleshape import CircleShape
from .constants import ASTEROID_MIN_RADIUS
import pygame
import random
from .explosion_effect import Line


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            explosion(self.position, self.radius)
        else:
            random_angle = random.uniform(20, 50)
            first_vector = self.velocity.rotate(random_angle)
            second_vector = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            child_1 = Asteroid(self.position.x, self.position.y, new_radius)
            child_1.velocity = first_vector * 1.2
            child_2 = Asteroid(self.position.x, self.position.y, new_radius)
            child_2.velocity = second_vector * 1.2
            self.kill()
            explosion(self.position, self.radius)


# helper function
def explosion(position, radius):
    for i in range(Line.num_lines):
        Line(i, position, radius)
