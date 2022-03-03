from turtle import *

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read()
        self.color("white")
        self.penup()
        self.width(5)
        self.setposition(-20, 260)
        self.ht()
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align="center", font=("courier", 15, "normal"))

    def read(self):
        with open("highscore.txt", mode="r") as file:
                self.highscore = int(file.read())

    def reset(self):
        if self.score > self.highscore:
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.score))
            self.read()
        self.score = 0
        self.updateScoreboard()

    def incrementScoreCard(self):
        self.score += 1
        self.updateScoreboard()