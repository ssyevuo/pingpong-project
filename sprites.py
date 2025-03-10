# Important imports
import pygame
from constants import *

# paddle class for the paddles in the game
class Paddle:
    # initializes the games recatngle with specified x and y
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED

    # Draws the paddle on the screen
    def draw(self, screen):
        pygame.draw.rect(screen, PADDLE_COLOR, self.rect)

    # moves the paddle either up or down
    def move(self, direction: str):
        # handle invalid directions 
        if direction not in ["up", "down"]:
            raise ValueError("Invalid direction, Must be 'up' or 'down'")
        
        if direction == "up":
            self.rect.y -= self.speed
        elif direction == "down":
            self.rect.y += self.speed

        #ensure the paddle is always in the game screen boundaries
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > HEIGHT - PADDLE_HEIGHT:
            self.rect.y = HEIGHT - PADDLE_HEIGHT

# ball Class for the ball in the game
class Ball:
    # initializes the balls rectangle
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X # sets the balls speed horizontally
        self.speed_y = BALL_SPEED_Y # sets the balls speed vertically

    # draws the ball with the ball color
    def draw(self, screen):
        pygame.draw.circle(screen, BALL_COLOR, self.rect.center, BALL_SIZE // 2)

    # updates the balls position by adding its speed
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y