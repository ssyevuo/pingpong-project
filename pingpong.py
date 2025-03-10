# Initializes pygame and creates the game window

#import important files
import pygame
from constants import *
from sprites import Paddle, Ball

pygame.init()

#create thegame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Paddle instance
paddle1 = Paddle(50, HEIGHT // 2 - PADDLE_HEIGHT // 2)
paddle2 =  Paddle(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2)

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Game logic

    screen.fill(BLACK)

    paddle1.draw(screen)
    paddle2.draw(screen)
    ball.draw(screen)
    ball.move()

    pygame.display.flip()

pygame.quit()