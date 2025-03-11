# Pygame Ping Pong Project

## About the project

A simple ping pong game built with Pygame, designed for a fun and engaging experience. The game features:
- An increase in game speed as the game progresses to enhance the challange
- Clear and responsive controls to ensure ease while playing
- Start and game over screens with instructions at the start screen.

## Setup

1. Clone the repository: `git clone git@github.com:ssyevuo/pingpong-project.git`
2. Navigate to the project directory: `cd pingpong-project`
3. Create and actgivate the virtual environment (make use of pipenv): `pipenv install then pipenv shell`
4. Install Pygame: `pip install pygame`
5. Run the game: `python pingpong.py`

## Controls
 ### Player 1
    - U: Move up Paddle
    - Y: Move Down Paddle

 ### Player 2
    - UP: Move paddle up
    - DOWN: Move paddle down

 ### Start/ Restart Game
    - SPACE: Start or restart the game after game over

 ### Delete high scores
    - C: Clear all the high scores 

## Features

* **Game State:** Clear start and game over screens for clarity
* **High Scores:** The game tracks the high scores by storing them using SQLite, and displays them on the start screen 
* **Responsive Controls:** Contains usage of controls to ensure the movement of the paddle for ease in playing

## Code Structure

- `pingpong.py`: Includes the game logic that is the game states
- `sprites.py`: Contains the Paddle and Ball classes 
- `utils.py`: Contains the database operations, the ball reset, obtains the scores, organizes the top 5 highscores and the delete function
- `constants.py`: Stores the game constants such as the agme color scheme, sizes and speeds
- `highscores.db`: database that stores highscores

## Future Improvements

- Add sound effects to make the game more fun
- Implement an Bot opponent incase the player is just one
- Allow players to use their names while playing 

## Contibuting

- Contributions are welcome! Submit a pull requests to suggest improvements or report bugs

## License
- This project is licensed under the MIT License. See the LICENSE file for details

## Contact
- If you have any questions or feedback, feel free to reach out:-> Email: `shakirasyevuo@gmail.com`