import pygame
import math


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):  # for grouping asteroids as a group of units
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, "White", self.triangle(), 2)

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, target):
        distance = self.position.distance_to(target.position)
        if distance <= (self.radius + target.radius):
            return True
        else:
            return False

    def triangle_collision(self, triangle_shaped_object):
        vertices = triangle_shaped_object.triangle()
        for i in range(3):
            edge_start = vertices[i]
            edge_end = vertices[(i + 1) % 3]

            center = self.position
            d = edge_end - edge_start  # that's our edge
            f = edge_start - center

            ######### Pure math, how a line intersects a circle
            # Quadratic equation coefficients: at² + bt + c = 0
            a = d.dot(d)
            b = 2 * f.dot(d)
            c = f.dot(f) - self.radius * self.radius

            discriminant = b * b - 4 * a * c

            # If discriminant >= 0, line intersects circle
            if discriminant >= 0:
                discriminant = math.sqrt(discriminant)
                t1 = (-b - discriminant) / (2 * a)
                t2 = (-b + discriminant) / (2 * a)

                # Check if intersection occurs within line segment (0 <= t <= 1)
                if (0 <= t1 <= 1) or (0 <= t2 <= 1):
                    return True
