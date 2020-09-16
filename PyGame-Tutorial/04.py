# pyggame.draw allows to draw simple shapes to
# surface - rectangler, polygn, circle, ellipse
# The functions have in common that they take-
# a surface object as first argument, color second
# argument, width third parameter return a Rect 
# object. If width is 0 shape is filled
import pygame, sys
from pygame.locals import *

pygame.init()

screen_width = 650
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
BLACK = (0,0,0)
GRAY = (127,127,127)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGNETA = (255,0,255)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, RED, (50,20,120,100))
    pygame.draw.rect(screen, GREEN, (100,60,120,100))
    pygame.draw.rect(screen, BLUE, (150, 100, 120, 100))
    pygame.draw.rect(screen, RED, (350,20,120,100), 1)
    pygame.draw.rect(screen, GREEN, (400,60,120,100), 4)
    pygame.draw.rect(screen, BLUE, (450, 100, 120, 100), 8)

    pygame.draw.ellipse(screen, RED, (50,220,120,100))
    pygame.draw.ellipse(screen, GREEN, (100,260,120,100))
    pygame.draw.ellipse(screen, BLUE, (150, 300, 120, 100))
    pygame.draw.ellipse(screen, RED, (350,220,120,100), 1)
    pygame.draw.ellipse(screen, GREEN, (400,260,120,100), 4)
    pygame.draw.ellipse(screen, BLUE, (450, 300, 120, 100), 8)
    pygame.display.update()

pygame.quit()