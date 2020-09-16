import pygame, sys
from pygame.locals import *

pygame.init()

screen_width = 1000
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
        elif event.type == MOUSEMOTION:
            print(event)
    
    pygame.display.update()

pygame.quit()