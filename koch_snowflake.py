import turtle
import math

def draw_koch(t, p1, p5, it):
    if it == 0:
        t.penup()
        t.goto(p1)
        t.pendown()
        t.goto(p5)
        return

    dx = (p5[0] - p1[0]) / 3
    dy = (p5[1] - p1[1]) / 3

    x1 = p1[0] + dx
    y1 = p1[1] + dy

    x3 = p1[0] + 2 * dx
    y3 = p1[1] + 2 * dy

    x2 = x1 + (x3 - x1) / 2 + math.sqrt(3) * (y3 - y1) / 2
    y2 = y1 + (y3 - y1) / 2 - math.sqrt(3) * (x3 - x1) / 2


    draw_koch(t, p1, (x1, y1), it - 1)
    draw_koch(t, (x1, y1), (x2, y2), it - 1)
    draw_koch(t, (x2, y2), (x3, y3), it - 1)
    draw_koch(t, (x3, y3), p5, it - 1)

WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.title("Koch Snowflake")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.pensize(2)
t.pencolor("black")
t.speed(0)

p0 = (0, 250)
p1 = (-200, -100)
p2 = (200, -100)

it = 3
draw_koch(t, p0, p1, it)
draw_koch(t, p1, p2, it)
draw_koch(t, p2, p0, it)

screen.mainloop()
