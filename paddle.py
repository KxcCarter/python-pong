from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.goto(-280, 0)
        self.paddle_segments = []
        self.create_paddle()

    def create_paddle(self):
        for _ in range(0, 3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            self.paddle_segments.append(new_segment)

    # Add controls here?