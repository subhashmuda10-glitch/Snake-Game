from turtle import Turtle
position=[(0,0),(-20,0),(-40,0)]
dist=20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for i in position:
            part = Turtle(shape="square")
            part.speed(0)
            part.penup()
            part.color("white")
            part.goto(i)
            self.segments.append(part)

    def move(self):
        for s in range(len(self.segments)- 1, 0, -1):
            new_x = self.segments[s - 1].xcor()
            new_y = self.segments[s - 1].ycor()
            self.segments[s].goto(new_x, new_y)
        self.head.forward(dist)

    def increase(self):
        part1 = Turtle(shape="square")
        part1.speed(80)
        part1.penup()
        part1.color("white")
        l=len(self.segments)
        x1=self.segments[l-1].xcor()
        y1=self.segments[l-1].ycor()
        part1.goto(x1, y1)
        self.segments.append(part1)

    def length(self):
        l=len(self.segments)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]


    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)


