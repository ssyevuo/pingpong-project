# import necessary files
import sqlite3
import pygame
from constants import *

# reset ball function
def reset_ball(ball):
    # moves the ball to the center of the screen thats where it starts
    ball.rect.x = WIDTH // 2 - BALL_SIZE // 2
    ball.rect.y = HEIGHT // 2 - BALL_SIZE // 2

    ball.speed_x = BALL_SPEED_X * (-1 if ball.speed_x < 0 else 1) # reset ball direction
    ball.speed_y = BALL_SPEED_Y # reset y speed.

def init_db():
    # connect with the SQLite database 
    conn = sqlite3.connect('highscores.db')
    c = conn.cursor()
    # creates a table scores if it doesnt exist
    c.execute('''CREATE TABLE IF NOT EXISTS scores
              (player text, score integer)''')
    conn.commit()
    conn.close()

init_db()  # helps initialize the database

# helps insert a new score to the list
def keep_score(player, score):
    conn = sqlite3.connect('highscores.db')
    c = conn.cursor()
    c.execute("INSERT INTO scores VALUES (?, ?)", (player, score))
    conn.commit()
    conn.close()

# selects the top 5 scores from the table
def get_highscores():
    conn = sqlite3.connect('highscores.db')
    c = conn.cursor()
    c.execute("SELECT player, score FROM scores ORDER BY score DESC LIMIT 5") # selects the top 5 scores
    highscores = c.fetchall()
    conn.close()
    return highscores

# to delete from the scores
def del_highscores():
    conn = sqlite3.connect('highscores.db')
    c = conn.cursor()
    c.execute("DELETE from scores")
    conn.commit()
    conn.close()


