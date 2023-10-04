from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.goto(0,0)
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("white")
        self.speed("fastest")
        self.move_x = 10
        self.move_y = 10

    def moveBall(self):
        new_y = self.ycor() +self.move_y
        new_x=self.xcor() + self.move_x
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1
    def bounce_x(self):
        self.move_x *= -1

    def miss(self):
        self.home()
        self.bounce_x()

