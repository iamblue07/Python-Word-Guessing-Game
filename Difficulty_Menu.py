import pygame
import pygame_menu
from screeninfo import get_monitors

primary_monitor = get_monitors()[0]
width = primary_monitor.width
height = primary_monitor.height

clock = pygame.time.Clock()

running = True

pygame.init()

screen = pygame.display.set_mode((width, height))


def difficulty_input(difficulty):
    return difficulty


while running:
    menu = pygame_menu.Menu('Difficulty', width / 2, height / 2,
                            theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button('Easy', difficulty_input(1))
    menu.add.button('Medium', difficulty_input(2))
    menu.add.button('Hard', difficulty_input(3))
    menu.add.button('Very Hard', difficulty_input(4))

    menu.mainloop(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
