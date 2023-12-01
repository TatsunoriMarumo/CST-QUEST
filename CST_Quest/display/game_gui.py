"""
Tatsunori Marumo
A01327744
Ephraim Hsu
A01366848
"""

import pygame
from pygame.locals import *

pygame.init()

screen_width = 850
screen_height = int(screen_width * 0.8)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("CST QUEST")

bg_image = pygame.image.load("")

running = True
while running:

    screen.blit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()
pygame.quit()

