import pygame
import pygame_gui


def menuUI():
    pygame.init()

    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("THE MENU")

    manager = pygame_gui.UIManager(screen_size, "game/menu_UI/theme.json")
    play_btn = pygame_gui.elements.UIButton(
        pygame.Rect(300, 250, 200, 50), "Play", manager
    )
    quit_btn = pygame_gui.elements.UIButton(
        pygame.Rect(300, 350, 200, 50), "Quit", manager
    )

    clock = pygame.time.Clock()
    running = True

    while running:
        time_delta = clock.tick(60) / 1000.0  # 0.016 s

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_btn:
                    return "play"
                elif event.ui_element == quit_btn:
                    return "quit"

            manager.process_events(event)

        screen.fill((0, 0, 0))
        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.update()
