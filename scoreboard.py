from turtle import Turtle


FONT_PARAMS = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.goto(0, 200)
        self.update_scores()

    def update_scores(self):
        self.write(f"{self.left_score} | {self.right_score}", align="center", font=FONT_PARAMS)

    def add_point(self, side):
        if side == 'left':
            self.left_score += 1
        else:
            self.right_score += 1
        self.clear()
        self.update_scores()
