import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def draw_axes(t, width, height):
    t.pencolor("black")
    t.pensize(1)

    # X-axis
    t.penup(); t.goto(-width // 2, 0); t.pendown()
    t.goto(width // 2, 0)
    t.penup(); t.goto(width // 2 - 10, 10); t.write("X", align="center", font=("Arial", 12, "normal"))

    # Y-axis
    t.penup(); t.goto(0, -height // 2); t.pendown()
    t.goto(0, height // 2)
    t.penup(); t.goto(10, height // 2 - 20); t.write("Y", align="center", font=("Arial", 12, "normal"))
    t.penup()

def put_pixel(t, x, y, color="lime"):
    t.penup()
    t.goto(int(x), int(y))
    t.pencolor(color)
    t.dot(2)

def plot_octant_points(t, xc, yc, x, y, color):
    put_pixel(t, xc + x, yc + y, color)
    put_pixel(t, xc + y, yc + x, color)
    put_pixel(t, xc - y, yc + x, color)
    put_pixel(t, xc - x, yc + y, color)
    put_pixel(t, xc - x, yc - y, color)
    put_pixel(t, xc - y, yc - x, color)
    put_pixel(t, xc + y, yc - x, color)
    put_pixel(t, xc + x, yc - y, color)

def midpoint_circle(t, center: Point, r: int, color="lime"):
    x = 0
    y = r

    p = 1 - r

    plot_octant_points(t, center.x, center.y, x, y, color)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

        plot_octant_points(t, center.x, center.y, x, y, color)

WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Midpoint Circle Drawing (8-way Symmetry)")
screen.bgcolor("white")
screen.tracer(2, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

draw_axes(t, WIDTH, HEIGHT)

C = Point(-150, 50)
midpoint_circle(t, C, 120, color="black")

C2 = Point(180, -60)
midpoint_circle(t, C2, 80, color="black")

C3 = Point(0, 200)
midpoint_circle(t, C3, 40, color="black")

turtle.done()
