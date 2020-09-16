# The best way to decode many keys is to use a Dictionary. We don't
# need to define if-else cases for all different keys.
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("HELLO WORLD")
BLACK = (0,0,0)
GRAY = (127,127,127)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGNETA = (255,0,255)
key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE, K_y:YELLOW, K_c:CYAN, K_m:MAGNETA, K_w:WHITE}
exit_game = False
background = GRAY

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]

    screen.fill(background)
    pygame.display.update()

pygame.quit()