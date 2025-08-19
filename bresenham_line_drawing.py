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
    t.penup(); t.goto(width // 2 - 10, 10); t.write("X", font=("Arial", 12, "normal"))

    # Y-axis
    t.penup(); t.goto(0, -height // 2); t.pendown()
    t.goto(0, height // 2)
    t.penup(); t.goto(10, height // 2 - 20); t.write("Y", font=("Arial", 12, "normal"))
    t.penup()

def put_pixel(t, x, y, color="lime"):
    t.penup()
    t.goto(x, y)
    t.pencolor(color)
    t.dot(2)

def label(t, p: Point, text, color="black"):
    t.penup(); t.goto(p.x + 6, p.y + 6)
    t.pencolor(color); t.write(text, font=("Arial", 10, "normal"))
    t.penup()

def bresenham_line(t, p1: Point, p2: Point, color="black"):
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = abs(y2 - y1)
    sx = 1
    sy = 1 if y2 >= y1 else -1

    if dy <= dx:
        p = 2 * dy - dx
        x, y = x1, y1
        put_pixel(t, x, y, color)
        for _ in range(dx):
            x += sx
            if p < 0:
                p += 2 * dy
            else:
                y += sy
                p += 2 * dy - 2 * dx
            put_pixel(t, x, y, color)
    else:
        p = 2 * dx - dy
        x, y = x1, y1
        put_pixel(t, x, y, color)
        for _ in range(dy):
            y += sy
            if p < 0:
                p += 2 * dx
            else:
                x += sx
                p += 2 * dx - 2 * dy
            put_pixel(t, x, y, color)

if __name__ == "__main__":
    WIDTH, HEIGHT = 800, 600
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Bresenham Line Drawing Algorithm")
    screen.bgcolor("white")
    screen.tracer(2, 0)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    draw_axes(t, WIDTH, HEIGHT)

    A = Point(-300, -100)
    B = Point(250, 50)
    C = Point(-200, 200)
    D = Point(100, -250)
    G = Point(-200, 100)
    H = Point(120, 100)

    for (p, q, col, name1, name2) in [
        (A, B, "black",  "A", "B"),
        (C, D, "black","C", "D"),
        (G, H, "black","G","H"),
    ]:
        label(t, p, name1)
        label(t, q, name2)
        bresenham_line(t, p, q, color=col)
        
    turtle.done()
