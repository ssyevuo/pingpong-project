# Pygame Ping Pong Project

## About the project

A simple ping pong game built with Pygame, designed for a fun and engaging experience. The game features
- An increase in game speed as the game progresses to enhance the challange
- Clear and responsive controls to ensure ease while playing
- Start and game over screens with instructions at the start screen.

## Setup

1. Clone the repository: `git clone git@github.com:ssyevuo/pingpong-project.git`
2. Navigate to the project directory: `cd pingpong-project`
3. Create and actgivate the virtual environment (make use of pipenv): `pipenv install then pipenv shell`
4. Install Pygame: `pip install pygame`
5. Run the game: `python pingpong.py`

### Constants

The game's constants (window dimensions, colors for the color scheme, paddle and ball size, speeds) are all defined in the constants.py

### Game Window

- The game window is created in `pingpong.py` using Pygame.
- he window first initializes with a dark background

### Paddle Class

- The `Paddle` class is defined in the `sprites.py`.
- Represents a paddle in the game and includes methods for drawing and moving the paddle around.
- Paddle movement is controlled by the key board keys U ANd Y for paddle1 and UP and DOWN  arrow keys for paddle2
- Collision detected between the ball and the paddle is implemented using `pygame.Rect.colliderect()`.
- The ball's horizontal speed is reversed upon collision with either of the two paddles.


### Ball Class

- The `Ball` class is defined in the `sprites.py`
- Represents the ball in the game and has methods for drawing and moving the ball.
- The ball moves according to its `speed_x` and `speed_y` attributes.
- When collision is detected the vertical speed is reversed.
- The balls speed increases after each paddle hit, hence increasing the difficulty of the game
- The speed resets when a player scores

### Scoring

- the scoring system stracls the scores of both the players dynamically at the top of the screen

### Reset ball function
- The reset ball function in `utils.py` is sed to reset the position ofthe ball


### Game States
- The game has a start and game over screens.
- The start screen prompts the user to press space in order to start the game 
- The game over declares the winner and the players can restart the game

### Controls
 #### Player 1
    - U: Move up Paddle
    - Y: Move Down Paddle

 #### Player 2
    - UP: Move paddle up
    - DOWN: Move paddle down

 #### Start/ Restart Game
    - SPACE: Start or restart the game after game over

 #### Delete high scores
    - C: Clear all the high scores 

## License
- This project is licensed under the MIT License. See the LICENSE file for details

## Contact
- If you have nay questions or feedback, feel free to reach out:-> Email: `shakirasyevuo@gmail.com`