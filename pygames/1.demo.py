import pygame
import sys

pygame.init()
pygame.display.set_mode(size=(400, 400))
pygame.display.set_caption("demo")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
