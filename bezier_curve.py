import turtle

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def bezier_function(k, n, u):
    return nCr(n, k) * (u ** k) * ((1 - u) ** (n - k))

def draw_axes(t, width, height):
    t.pencolor("black")
    t.pensize(1)

    t.penup()
    t.goto(-width / 2, 0)
    t.pendown()
    t.goto(width / 2, 0)
    t.write("X", align="center", font=("Arial", 12, "normal"))

    t.penup()
    t.goto(0, -height / 2)
    t.pendown()
    t.goto(0, height / 2)
    t.write("Y", align="center", font=("Arial", 12, "normal"))
    t.penup()

def draw_bezier(t, points):

    # Draw control points
    t.pencolor("black")
    for x, y in points:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(10)

    n = len(points) - 1
    eps = 0.001
    t.pencolor("black")

    prev = None
    u = 0.0
    while u <= 1.0:
        x = 0
        y = 0
        for k in range(n + 1):
            b = bezier_function(k, n, u)
            x += points[k][0] * b
            y += points[k][1] * b
        if prev:
            t.penup()
            t.goto(prev)
            t.pendown()
            t.goto(x, y)
        prev = (x, y)
        u += eps

WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.title("Bézier Curve")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("white")
screen.tracer(2, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0.0)
draw_axes(t, WIDTH, HEIGHT)
t.pensize(2)

control_points = [
    (-150, 100),
    (-50, -100),
    (50, 100),
    (150, 0)
]

draw_bezier(t, control_points)

screen.mainloop()
