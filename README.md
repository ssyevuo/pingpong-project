# pingpong-project

A simple ping pong game built with Pygame

## Setup

1. Clone the repository: `git clone `
2. Navigate to the project directory: `cd pingpong-project`
3. Create and actgivate the virtual environment (make use of pipenv): `pipenv install then pipenv shell`
4. Install Pygame: `pip install pygame`
5. Run the game: `python pingpong.py`

## Constants

The game's constants (window dimensions, colors, paddle and ball size, speeds) are all defined in the constants.py

## Game Window

- The game window is created in `pingpong.py` using Pygame.
- he window first initializes with a black background

## Paddle Class

- The `Paddle` class is defined in the `sprites.py`.
- Represents a paddle in the game and includes methos for drawing and moving the paddle around.

## Ball Class

- The `Ball` class is defined in the `sprites.py`
- Represents the ball in the game and has methods for drawing and moving the ball.
