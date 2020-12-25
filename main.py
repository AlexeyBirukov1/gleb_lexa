import pygame

pygame.init()

win = pygame.display.set_mode((800, 450))

pygame.display.set_caption("GAMER")

bg = pygame.image.load('sp/backgroung.png')
playerStand = [pygame.image.load('sp/paddle1.png'), pygame.imag