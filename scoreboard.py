from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0

    def add_point(self, side):
        if side == 'left':
            self.left_score += 1
        else:
            self.right_score += 1
