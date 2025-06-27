import pygame
import random
from .constants import *
import csv
from datetime import datetime
import os


class Score:
    def __init__(self, x, y, color):
        self.score = 0
        self.position = (x, y)
        self.high_score_position = (x, y + 30)
        self.font = pygame.font.Font(None, 36)
        self.color = color
        self.high_score = 0

        if os.path.exists("high_score.csv"):
            with open("high_score.csv", mode="r", newline="") as f:
                list_of_rows = csv.reader(f)
                for row in list_of_rows:
                    if self.high_score < int(row[0]):
                        self.high_score = int(row[0])

    def draw(self, screen):
        text_score = self.font.render(f"Score: {self.score}", True, self.color)
        text_high_score = self.font.render(
            f"High Score: {self.high_score}", True, "orange"
        )
        screen.blit(text_score, self.position)
        screen.blit(text_high_score, self.high_score_position)

    def add(self, target_radius):
        if target_radius == 60:
            self.score += ASTEROID_LVL_3
        elif target_radius == 40:
            self.score += ASTEROID_LVL_2
        elif target_radius == 20:
            self.score += ASTEROID_LVL_3

    def sub(self):
        self.score -= 100

    def save_score(self):
        self.high_score = self.score
        with open("high_score.csv", mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                [self.high_score, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
            )
