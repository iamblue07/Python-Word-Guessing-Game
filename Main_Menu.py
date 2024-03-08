import pygame
import Game_Functions as GF
import Menu_Functions as MF

running = True

pygame.init()

MF.clock.tick(60)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    MF.screen.fill("black")

    MF.main_menu()

    pygame.display.flip()

pygame.quit()
