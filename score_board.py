from turtle import Turtle,Screen
ALIGNMENT="left"
FONT="Courier",50,"normal"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(150,300)
        self.score1=0
        self.score2 = 0
        self.color("white")
        self.write(f"{self.score1}",ALIGNMENT,font=FONT)

    def other(self):
        self.goto(-150, 300)
        self.write(f"{self.score1}", ALIGNMENT, font=FONT)
