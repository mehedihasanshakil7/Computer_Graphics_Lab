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
screen.title("2D Translation")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(1)

draw_axes(t, WIDTH, HEIGHT)
t.pensize(2)
original_coordinates = [
    (-50, -50),
    (100, -50),
    (100, 50),
    (-50, 50)
]
tx, ty = (100, 75)
translated_coordinates = []

for point in original_coordinates:
    x, y = point
    new_x = x + tx
    new_y = y + ty
    translated_coordinates.append((new_x, new_y))

draw_polygon(t, original_coordinates, "lightgray")
draw_polygon(t, translated_coordinates, "black")

screen.mainloop()