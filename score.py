from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.s=0
        with open("high_score.txt", mode="r") as file:
            self.highscore=int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0,y=365)
        self.speed("fastest")
        self.write(f"Score : {self.s}  High Score : {self.highscore}",align="center",font=("Aerial",18,"normal"))

    def update(self):
        self.clear()
        self.write(f"Score : {self.s} High Score : {self.highscore}", align="center", font=("Aerial", 18, "normal"))

    def reset(self):
        if self.s > self.highscore:
            self.highscore=self.s
            with open("high_score.txt", mode="w")as file:
                file.write(f"{self.highscore}")
        self.s=0
        self.update()

    def increase(self):
        self.s+=1
        self.update()

    #def gameover(self):
     #   self.goto(0,0)
      #  self.write("GAME OVER",align="center", font=("Aerial", 24, "normal"))