# Important imports
import pygame
from constants import *

# paddle class
class Paddle:
    # initializes the games recatngle with specified x and y
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED

    # Draws the paddle on the screen
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

    # moves the paddle either up or down
    def move(self, direction):
        if direction == "up":
            self.rect.y -= self.speed
        elif direction == "down":
            self.rect.y += self.speed

        #ensure the paddle is always in the game screen boundaries
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > HEIGHT - PADDLE_HEIGHT:
            self.rect.y = HEIGHT - PADDLE_HEIGHT