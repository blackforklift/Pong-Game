from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.goto(position)

    def moveUp(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def moveDown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



