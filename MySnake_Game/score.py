from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.game_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write(f"SCORE: {self.game_score}", False, align='center')

    def score_refresh(self):
        self.clear()
        self.game_score += 1
        self.write(f"SCORE: {self.game_score}", False, align='center')

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align='center')
