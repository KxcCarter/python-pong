from turtle import Turtle


FONT_PARAMS = ("Courier", 80, "normal")
POINTS_TO_WIN = 2


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.winner = ''
        self.waiting_for_winner = True
        self.goto(0, 200)
        self.update_scores()

    def update_scores(self):
        self.write(f"{self.left_score} | {self.right_score}", align="center", font=FONT_PARAMS)
        self.check_for_winner()

    def add_point(self, side):
        if side == 'left':
            self.left_score += 1
        else:
            self.right_score += 1
        self.clear()
        self.update_scores()

    def check_for_winner(self):
        if self.left_score >= POINTS_TO_WIN or self.right_score >= POINTS_TO_WIN:
            self.waiting_for_winner = False
            self.announce_winner()

    def announce_winner(self):
        if self.left_score >= POINTS_TO_WIN:
            self.winner = 'Left Player'
        elif self.right_score >= POINTS_TO_WIN:
            self.winner = 'Right Player'

        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT_PARAMS)
        self.goto(0, -50)
        self.write(f"{self.winner} wins", align="center", font=("Courier", 40, "normal"))