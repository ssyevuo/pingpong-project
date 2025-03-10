# Initializes pygame and creates the game window

#import important files
import pygame
from constants import *

pygame.init()

#create thegame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Game logic

    screen.fill(BLACK)

    pygame.display.flip()

pygame.quit()