from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

import time
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800 , height=600)
screen.title("PONG !")

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.onkeypress(r_paddle.moveUp, "Up")
screen.onkeypress(r_paddle.moveDown, "Down")

screen.onkeypress(l_paddle.moveUp, "w")
screen.onkeypress(l_paddle.moveDown, "s")

ball = Ball()


screen.listen()
game_is_on=True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    ball.moveBall()
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounceBall()




screen.exitonclick()