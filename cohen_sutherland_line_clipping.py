import turtle

# Clipping window boundaries
x_left, x_right = -100, 300
y_bottom, y_top = -50, 200

# Region codes
LEFT, RIGHT, BOTTOM, TOP = 1, 2, 4, 8

def draw_line(t, x1, y1, x2, y2, color):
    t.pencolor(color)
    t.pensize(2)
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
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

def region_code(x, y):
    code = 0
    if x < x_left:
        code |= LEFT
    elif x > x_right:
        code |= RIGHT
    if y < y_bottom:
        code |= BOTTOM
    elif y > y_top:
        code |= TOP
    return code

def cohen_sutherland(t, x1, y1, x2, y2, color):
    code1 = region_code(x1, y1)
    code2 = region_code(x2, y2)

    while True:
        if not (code1 | code2):
            draw_line(t, x1, y1, x2, y2, color)
            break
        elif code1 & code2:
            break
        else:
            if code1:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_top - y1) / (y2 - y1)
                y = y_top
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_bottom - y1) / (y2 - y1)
                y = y_bottom
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_right - x1) / (x2 - x1)
                x = x_right
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_left - x1) / (x2 - x1)
                x = x_left

            if code_out == code1:
                x1, y1 = x, y
                code1 = region_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = region_code(x2, y2)

WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.title("Cohen-Sutherland Line Clipping")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

draw_axes(t, WIDTH, HEIGHT)

# Draw the clipping rectangle
t.pencolor("black")
t.penup()
t.goto(x_left, y_bottom)
t.pendown()
t.goto(x_right, y_bottom)
t.goto(x_right, y_top)
t.goto(x_left, y_top)
t.goto(x_left, y_bottom)
t.penup()

lines = [
    (90, 60, 150, 150),
    (50, 250, 80, 20),
    (-180, -30, 300, 300),
    (-200, -10, -150, 100),
    (-200, 50, 400, 50)
]
for x1, y1, x2, y2 in lines:
    draw_line(t, x1, y1, x2, y2, 'lightgray')
    cohen_sutherland(t, x1, y1, x2, y2, "black")

screen.mainloop()
