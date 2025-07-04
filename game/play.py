import pygame
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_X, PLAYER_Y
from game.player import Player
from game.asteroid import Asteroid
from game.asteroidfield import AsteroidField
from game.shot import Shot
from game.score import Score
from game.life_manager import LifeManager
from game.explosion_effect import Line
import os


def play():
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    explosion_lines = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Shot.containers = (bullets, drawable, updatable)
    LifeManager.containers = drawable
    Line.containers = (drawable, updatable, explosion_lines)

    AsteroidField()
    player = Player(PLAYER_X, PLAYER_Y)
    score = Score(SCREEN_WIDTH / 2 - 50, 20, "gold")
    life_manager = LifeManager()

    while True:
        screen.fill("black")
        score.draw(screen)
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for obj in asteroids:
            if obj.triangle_collision(player):
                if not life_manager.life_list:
                    print("Game Over!")  # checks if any lives are left
                    return
                else:
                    score.sub()
                    life_manager.lose_life()
                    player.position = pygame.Vector2(
                        PLAYER_X, PLAYER_Y
                    )  # teleports to the starting position
                    player.acceleration = 0
                    for asteroid in asteroids:
                        asteroid.kill()
                    for line in explosion_lines:
                        line.kill()

            for bullet in bullets:
                if obj.collision(bullet):
                    obj.split()
                    bullet.kill()
                    score.add(obj.radius)

        pygame.display.flip()  # double-buffer mechanic, this is basically a copy-paste function, rendering...

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                score.save_score()
                return

        dt = clock.tick(60) / 1000
