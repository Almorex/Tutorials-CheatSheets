# Colors are defined as RGB Values in Pygame although you can
# Also use Hex Code
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600,600))

BLACK = (0,0,0)
GRAY = (127,127,127)
WHITE = (256, 256, 256)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAAGNETA = (255,0,255)

exit_game = False
background = GRAY

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED
            if event.key == pygame.K_g:
                background = GREEN
    
    background = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    screen.fill(background)
    pygame.display.update()

pygame.quit()