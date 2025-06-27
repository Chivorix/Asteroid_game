from .constants import *
import pygame


class LifeManager(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.life_list = []
        for i in range(3):
            life = Life()
            self.life_list.append(life)

    def draw(self, screen):
        position = FIRST_LIFE
        for life in self.life_list:
            life.draw(screen, position)
            position = [(x + 50, y) for (x, y) in position]

    def lose_life(self):
        self.life_list.pop()


class Life:
    def __init__(self):
        self.color = "white"

    def draw(self, screen, position):
        pygame.draw.polygon(screen, self.color, position)
