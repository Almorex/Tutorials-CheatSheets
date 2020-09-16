import pygame
# Importing Pygame

pygame.init()
# Initialises Pygame

screen = pygame.display.set_mode((640, 240))
# display.set_mode sets the screen size and returns a surface object
# which we store in variable screen

exit_game = False

while not exit_game: # Main Game Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

pygame.quit()
# Quit Pygame