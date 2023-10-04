from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800 , height=600)
screen.title("PONG !")

scoreboard = Scoreboard()
ball = Ball()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.onkeypress(r_paddle.moveUp, "Up")
screen.onkeypress(r_paddle.moveDown, "Down")
screen.onkeypress(l_paddle.moveUp, "w")
screen.onkeypress(l_paddle.moveDown, "s")

screen.listen()

game_is_on=True

while game_is_on:

    time.sleep(0.1)
    screen.update()
    ball.moveBall()
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

 #detect paddles and ball contact

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() <= -320 and ball.distance(l_paddle) < 50:
       ball.bounce_x()
       ball.accelerate()

 #detect the miss then reset the ball's possition to home and then ball should start moving to other player

 #r paddle
    if ball.xcor() > 360 :
        ball.miss()
        scoreboard.l_point()
 # l paddle
    if ball.xcor() < -360:
        ball.miss()
        scoreboard.r_point()



screen.exitonclick()