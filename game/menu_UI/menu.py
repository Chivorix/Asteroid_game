import pygame
import pygame_gui


def menu():
    pygame.init()

    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("THE MENU")

    manager = pygame_gui.UIManager(screen_size, "theme.json")
    play_button = pygame_gui.elements.UIButton(
        pygame.Rect(300, 250, 200, 50), "Play", manager
    )

    clock = pygame.time.Clock()

    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0  # 0.016 s

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            manager.process_events(event)

        screen.fill((0, 0, 0))
        manager.update(time_delta)  # what to draw
        manager.draw_ui(screen)  # draw
        pygame.display.update()


menu()
