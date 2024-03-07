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


def start_the_game():
    # Do the job here !
    pass


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    menu = pygame_menu.Menu('Welcome', width/2, height/2,
                            theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)
    pygame.display.flip()

    clock.tick(60)


pygame.quit()
