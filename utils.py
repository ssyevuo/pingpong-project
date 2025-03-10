# necessary importants
import pygame
from constants import *

# reset ball function
def reset_ball(ball):
    ball.rect.x = WIDTH // 2 - BALL_SIZE // 2
    ball.rect.y = HEIGHT // 2 - BALL_SIZE // 2
    ball.speed_x = BALL_SPEED_X * (-1 if ball.speed_x < 0 else 1) # reset ball direction
    ball.speed_y = BALL_SPEED_Y # reset y speed.

