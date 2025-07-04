from game.play import play
from game.menu_UI.menu import menuUI
import pygame


def main():
    while True:
        action = menuUI()
        if action == "play":
            play()
        elif action == "quit":
            break
    pygame.quit()


if __name__ == "__main__":
    main()
