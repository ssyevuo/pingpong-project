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

# game state constants
GAME_STATE_START = 0
GAME_STATE_PLAYING = 1
GAME_STATE_GAME_OVER = 2
game_state = GAME_STATE_START

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if game_state == GAME_STATE_START:
        title_text = font.render("Ping Pong", True, TEXT_COLOR)
        player1_text = font.render("Player 1: U/Y", True, TEXT_COLOR)
        player2_text = font.render("Player 2: UP/DOWN", True, TEXT_COLOR)
        start_text = font.render("Press SPACE to start", True, TEXT_COLOR)

        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))
        screen.blit(player1_text, (WIDTH // 4 - player1_text.get_width() // 2, HEIGHT // 2 - 25))
        screen.blit(player2_text, (3 * WIDTH // 4 - player2_text.get_width() // 2, HEIGHT // 2 - 25))
        screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 + 50))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_state = GAME_STATE_PLAYING
        pygame.display.flip()
        continue # skip the rest of the loop
    
    # Game logic

    screen.fill(BACKGROUND_COLOR)

    if game_state == GAME_STATE_GAME_OVER:
        winner_text = font.render(f"Player {1 if score1 > score2 else 2} wins!", True, TEXT_COLOR)
        restart_text = font.render("Press SPACE to restart", True, TEXT_COLOR)
        screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 4))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_state = GAME_STATE_PLAYING
            score1 = 0
            score2 = 0
            reset_ball(ball)
        pygame.display.flip()
        continue

    if game_state == GAME_STATE_PLAYING:
        #returns a tuple of boolean to show the state of the keyboard key
        keys = pygame.key.get_pressed()

        # when u is pressed paddle 1 moves up and when d is pressed padde 1 moves donw
        if keys[pygame.K_u]:
            paddle1.move("up")
        if keys[pygame.K_y]:
            paddle1.move("down")
        # paddle 2 usses the UP and down Keys for the same function as the u and d keys
        if keys[pygame.K_UP]:
            paddle2.move("up")
        if keys[pygame.K_DOWN]:
            paddle2.move("down")

        ball.move()

        # checks for wall collisions and bounces it back the ball that is
        if ball.rect.y <= 0 or ball.rect.y >= HEIGHT - BALL_SIZE:
            ball.speed_y *= -1

        # ball and paddle collisions
        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.speed_x *= -1
            # increase the speed of the game as the game progresses
            if ball.speed_x > 0:
                ball.speed_x += 0.5
            else:
                ball.speed_x -= 0.5
            if ball.speed_y > 0:
                ball.speed_y += 0.5
            else:
                ball.speed_y -= 0.5
            
            # ensure that the speed does not get to 0
            if abs(ball.speed_x) < 1:
                ball.speed_x = 1 if ball.speed_x > 0 else -1
            if abs(ball.speed_y) < 1:
                ball.speed_y = 1 if ball.speed_y > 0 else -1


        # check if the ball goes off screen 
        if ball.rect.x <= 0:
            score2 += 1
            reset_ball(ball)
        elif ball.rect.x >= WIDTH - BALL_SIZE:
            score1 += 1
            reset_ball(ball)

        if score1 >= 5 or score2 >= 5:
            game_state = GAME_STATE_GAME_OVER

        paddle1.draw(screen)
        paddle2.draw(screen)
        ball.draw(screen)

    score_text1 = font.render(str(score1), True, TEXT_COLOR)
    score_text2 = font.render(str(score2), True, TEXT_COLOR)
    screen.blit(score_text1, (WIDTH // 4, 20))
    screen.blit(score_text2, (3 * WIDTH // 4, 20))

    # The middle net
    for y in range(0, HEIGHT, 20):
        net_rect = pygame.Rect(WIDTH // 2 - 2, y, 4, 10)
        pygame.draw.rect(screen, NET_COLOR, net_rect)


    pygame.display.flip()

pygame.quit()