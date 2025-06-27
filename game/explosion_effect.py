import pygame
import math


class Line(pygame.sprite.Sprite):
    num_lines = 12

    def __init__(self, i, asteroid_position, asteroid_radius):
        super().__init__(self.containers)
        self.center = asteroid_position
        self.radius = asteroid_radius
        if self.radius == 60:
            self.line_length = 40
        elif self.radius == 40:
            self.line_length = 25
        elif self.radius == 20:
            self.line_length = 10

        self.angle_degrees = i * (360 / Line.num_lines)
        self.angle = math.radians(self.angle_degrees)
        self.cos = math.cos(self.angle)
        self.sin = math.sin(self.angle)

        self.start_x = self.center[0] + int(self.radius * self.cos)
        self.start_y = self.center[1] + int(self.radius * self.sin)
        self.end_x = self.center[0] + int(
            (self.radius + self.line_length) * self.cos
        )  # Lengthen the line
        self.end_y = self.center[1] + int((self.radius + self.line_length) * self.sin)

        self.start = pygame.math.Vector2(self.start_x, self.start_y)
        self.end = pygame.math.Vector2(self.end_x, self.end_y)

    def draw(self, screen):
        pygame.draw.line(screen, "white", self.start, self.end, 2)

    def update(self, dt):
        if int(self.angle_degrees) == 0:
            self.start[0] += 40 * dt
        elif int(self.angle_degrees) == 30:
            self.start[0] += 40 * dt
            self.start[1] += 22 * dt
        elif int(self.angle_degrees) == 60:
            self.start[0] += 22 * dt
            self.start[1] += 40 * dt
        elif int(self.angle_degrees) == 90:
            self.start[1] += 40 * dt
        elif int(self.angle_degrees) == 120:
            self.start[0] -= 25 * dt
            self.start[1] += 40 * dt
        elif int(self.angle_degrees) == 150:
            self.start[0] -= 40 * dt
            self.start[1] += 25 * dt
        elif int(self.angle_degrees) == 180:
            self.start[0] -= 40 * dt
        elif int(self.angle_degrees) == 210:
            self.start[0] -= 40 * dt
            self.start[1] -= 25 * dt
        elif int(self.angle_degrees) == 240:
            self.start[0] -= 25 * dt
            self.start[1] -= 40 * dt
        elif int(self.angle_degrees) == 270:
            self.start[1] -= 40 * dt
        elif int(self.angle_degrees) == 300:
            self.start[0] += 25 * dt
            self.start[1] -= 40 * dt
        elif int(self.angle_degrees) == 330:
            self.start[0] += 40 * dt
            self.start[1] -= 25 * dt

        if self.start.distance_to(self.end) < 2:
            self.kill()
