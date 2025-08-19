import turtle

def draw_polygon(t, poly, color):
    t.pencolor(color)
    t.penup()
    t.goto(poly[0][0], poly[0][1])
    t.pendown()
    for i in range(len(poly)):
        next_vertex = poly[(i + 1) % len(poly)]
        t.goto(next_vertex[0], next_vertex[1])
    t.penup()

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

WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.title("2D Fixed-Point Scaling")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0.6)

draw_axes(t, WIDTH, HEIGHT)
t.pensize(2)

original_coordinates = [
    (200, 100),
    (150, 186),
    (50, 186),
    (0, 100),
    (50, 14),
    (150, 14)
]

# Calculate the centroid (fixed point)
n = len(original_coordinates)
xf = sum(x for x, y in original_coordinates) / n
yf = sum(y for x, y in original_coordinates) / n

sx, sy = 2, 2
scaled_coordinates = []

for x, y in original_coordinates:
    new_x = xf + (x - xf) * sx
    new_y = yf + (y - yf) * sy
    scaled_coordinates.append((new_x, new_y))

draw_polygon(t, original_coordinates, "lightgray")
draw_polygon(t, scaled_coordinates, "black")

screen.mainloop()
