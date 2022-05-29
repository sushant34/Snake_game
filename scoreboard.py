from turtle import Turtle
FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.score = 0
        self.write(f"Score : {self.score}", align="center", font=FONT)

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)