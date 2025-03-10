# Initializes pygame and creates the game window

#import important files
import pygame
from constants import *
from sprites import Paddle, Ball
from utils import reset_ball

pygame.init()

#create thegame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Paddle instance
paddle1 = Paddle(50, HEIGHT // 2 - PADDLE_HEIGHT // 2)
paddle2 =  Paddle(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2)

# Score variables
score1 = 0
score2 = 0

# font for the scores
font = pygame.font.Font(None, 36)

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

    #returns a tuple of boolean to show the state of the keyboard key
    keys = pygame.key.get_pressed()

    # when u is pressed paddle 1 moves up and when d is pressed padde 1 moves donw
    if keys[pygame.K_u]:
        paddle1.move("up")
    if keys[pygame.K_d]:
        paddle1.move("down")
    # paddle 2 usses the UP and down Keys for the same function as the u and d keys
    if keys[pygame.K_UP]:
        paddle2.move("up")
    if keys[pygame.K_DOWN]:
        paddle2.move("down")

    ball.draw(screen)
    ball.move()

    # checks for wall collisions and bounces it back the ball that is
    if ball.rect.y <= 0 or ball.rect.y >= HEIGHT - BALL_SIZE:
        ball.speed_y *= -1

    # ball and paddle collisions
    if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
        ball.speed_x *= -1

    # check if the ball goes off screen 
    if ball.rect.x <= 0:
        score2 += 1
        reset_ball(ball)
    elif ball.rect.x >= WIDTH - BALL_SIZE:
        score1 += 1
        reset_ball(ball)

    score_text1 = font.render(str(score1), True, WHITE)
    score_text2 = font.render(str(score2), True, WHITE)
    screen.blit(score_text1, (WIDTH // 4, 20))
    screen.blit(score_text2, (3 * WIDTH // 4, 20))


    pygame.display.flip()

pygame.quit()