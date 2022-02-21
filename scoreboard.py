#############################################################
#Date: 21.02.22                                             #
#Programmed by: Luka Henig (luka.henig@gmail.com)           #
#Curse: 100 Days of Code(udemy)                             #
#Description: Litle snake game to learn and understand      #
#python directories, files and paths                        #
#############################################################

#imports
from turtle import Turtle

#constants
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("src/data.txt") as data:      #open data file
           self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """update the score on screen, no parameters"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """reset score and update high_score in data, no parameters"""
        if self.score > self.high_score:
           self.high_score = self.score
           with open("src/data.txt", mode="w") as data:     #safe date in file
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        """display the game over text on the screen, no parameters"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """increase the score by one and update screen, no parameters"""
        self.score += 1
        self.update_scoreboard()
