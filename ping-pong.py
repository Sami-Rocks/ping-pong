import turtle
import winsound

win = turtle.Screen()
win.title("My Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


def paddle(position, ball_width=5):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.shapesize(stretch_wid=ball_width, stretch_len=1)
    paddle.color("white")
    paddle.penup()
    paddle.goto(position, 0)

    return paddle




paddle_a = paddle(-350)
paddle_b = paddle(350)
ball = paddle(0, 1)
ball.dx = 0.2
ball.dy = 0.2


score_a = 0
score_b = 0


pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))



def paddle_a_move_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
def paddle_a_move_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
def paddle_b_move_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
def paddle_b_move_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

win.listen()
win.onkeypress(paddle_a_move_up, 'w')
win.onkeypress(paddle_a_move_down, 's')
win.onkeypress(paddle_b_move_up, 'Up')
win.onkeypress(paddle_b_move_down, "Down")




while True:
    win.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
