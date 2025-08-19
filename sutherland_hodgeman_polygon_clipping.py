import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

wMin = Point(-50, -50)
wMax = Point(150, 100)

LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 3

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

def inside(p, edge):
    if edge == LEFT:
        return p.x >= wMin.x
    elif edge == RIGHT:
        return p.x <= wMax.x
    elif edge == BOTTOM:
        return p.y >= wMin.y
    elif edge == TOP:
        return p.y <= wMax.y

def intersect(p1, p2, edge):
    if p1.x != p2.x:
        m = (p2.y - p1.y) / (p2.x - p1.x)
    else:
        m = float('inf')

    if edge == LEFT:
        x = wMin.x
        y = p1.y + (wMin.x - p1.x) * m
    elif edge == RIGHT:
        x = wMax.x
        y = p1.y + (wMax.x - p1.x) * m
    elif edge == BOTTOM:
        y = wMin.y
        x = p1.x + (wMin.y - p1.y) / m if m != 0 else p1.x
    elif edge == TOP:
        y = wMax.y
        x = p1.x + (wMax.y - p1.y) / m if m != 0 else p1.x

    return Point(x, y)

def clip_polygon(points, edge):
    clipped = []
    for i in range(len(points)):
        curr = points[i]
        prev = points[i - 1]
        curr_in = inside(curr, edge)
        prev_in = inside(prev, edge)

        if prev_in and curr_in:
            clipped.append(curr)
        elif not prev_in and curr_in:
            clipped.append(intersect(prev, curr, edge))
            clipped.append(curr)
        elif prev_in and not curr_in:
            clipped.append(intersect(prev, curr, edge))
    return clipped

def draw_polygon(t, points, color):
    t.pensize(2)
    if not points:
        return
    t.pencolor(color)
    t.penup()
    t.goto(points[0].x, points[0].y)
    t.pendown()
    for p in points[1:] + [points[0]]:
        t.goto(p.x, p.y)
    t.penup()

def draw_clip_window(t):
    t.pencolor("black")
    t.penup()
    t.goto(wMin.x, wMin.y)
    t.pendown()
    t.goto(wMax.x, wMin.y)
    t.goto(wMax.x, wMax.y)
    t.goto(wMin.x, wMax.y)
    t.goto(wMin.x, wMin.y)
    t.penup()

star_points = [
    Point(  50, 150),
    Point( 100,  70),
    Point( 180,  70),
    Point( 110,  20),
    Point( 150, -70),
    Point(  50, -20),
    Point( -50, -70),
    Point( -10,  20),
    Point( -80,  70),
    Point(   0,  70)
]

WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Sutherland-Hodgman Polygon Clipping")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

draw_axes(t, WIDTH, HEIGHT)

draw_clip_window(t)
draw_polygon(t, star_points, "lightgray")

clipped = star_points
for edge in [LEFT, RIGHT, BOTTOM, TOP]:
    clipped = clip_polygon(clipped, edge)

draw_polygon(t, clipped, "black")

turtle.done()


# import turtle
# import time

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# # Clipping window boundaries
# wMin = Point(100, 100)
# wMax = Point(300, 250)

# # Clipping edge constants
# LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 3

# def draw_axes(t, width, height):
#     t.pencolor("white")
#     t.pensize(1)
#     t.penup()
#     t.goto(-width // 2, 0)
#     t.pendown()
#     t.goto(width // 2, 0)
#     t.write("X", align="center", font=("Arial", 12, "normal"))
#     t.penup()
#     t.goto(0, -height // 2)
#     t.pendown()
#     t.goto(0, height // 2)
#     t.write("Y", align="center", font=("Arial", 12, "normal"))
#     t.penup()

# def inside(p, edge):
#     if edge == LEFT:
#         return p.x >= wMin.x
#     elif edge == RIGHT:
#         return p.x <= wMax.x
#     elif edge == BOTTOM:
#         return p.y >= wMin.y
#     elif edge == TOP:
#         return p.y <= wMax.y

# def intersect(p1, p2, edge):
#     if p1.x != p2.x:
#         m = (p2.y - p1.y) / (p2.x - p1.x)
#     else:
#         m = float('inf')

#     if edge == LEFT:
#         x = wMin.x
#         y = p1.y + (wMin.x - p1.x) * m
#     elif edge == RIGHT:
#         x = wMax.x
#         y = p1.y + (wMax.x - p1.x) * m
#     elif edge == BOTTOM:
#         y = wMin.y
#         x = p1.x + (wMin.y - p1.y) / m if m != 0 else p1.x
#     elif edge == TOP:
#         y = wMax.y
#         x = p1.x + (wMax.y - p1.y) / m if m != 0 else p1.x

#     return Point(x, y)

# def clip_polygon(points, edge):
#     clipped = []
#     for i in range(len(points)):
#         curr = points[i]
#         prev = points[i - 1]
#         curr_in = inside(curr, edge)
#         prev_in = inside(prev, edge)

#         if prev_in and curr_in:
#             clipped.append(curr)
#         elif not prev_in and curr_in:
#             clipped.append(intersect(prev, curr, edge))
#             clipped.append(curr)
#         elif prev_in and not curr_in:
#             clipped.append(intersect(prev, curr, edge))
#     return clipped

# def draw_polygon(t, points, color, label=None):
#     if not points:
#         return
#     t.pencolor(color)
#     t.penup()
#     t.goto(points[0].x, points[0].y)
#     t.pendown()
#     for p in points[1:] + [points[0]]:
#         t.goto(p.x, p.y)
#     t.penup()
#     if label:
#         t.goto(points[0].x + 10, points[0].y + 10)
#         t.write(label, font=("Arial", 10, "normal"))

# def draw_clip_window(t):
#     t.pencolor("white")
#     t.penup()
#     t.goto(wMin.x, wMin.y)
#     t.pendown()
#     t.goto(wMax.x, wMin.y)
#     t.goto(wMax.x, wMax.y)
#     t.goto(wMin.x, wMax.y)
#     t.goto(wMin.x, wMin.y)
#     t.penup()

# # Star polygon (larger than window to demonstrate clipping)
# star_points = [
#     Point(200, 300), Point(250, 220), Point(330, 220),
#     Point(260, 170), Point(300, 80), Point(200, 130),
#     Point(100, 80), Point(140, 170), Point(70, 220),
#     Point(150, 220)
# ]

# # Setup turtle screen
# WIDTH, HEIGHT = 600, 400
# screen = turtle.Screen()
# screen.setup(WIDTH, HEIGHT)
# screen.title("Sutherland-Hodgman Clipping: Step-by-Step")
# screen.bgcolor("black")

# t = turtle.Turtle()
# t.speed(1)
# t.pensize(2)

# # Draw scene
# draw_axes(t, WIDTH, HEIGHT)
# draw_clip_window(t)
# draw_polygon(t, star_points, "gray", "Original")
# time.sleep(1)

# # Step-by-step clipping
# clipped = star_points
# colors = ["red", "yellow", "cyan", "lime"]
# labels = ["After LEFT", "After RIGHT", "After BOTTOM", "After TOP"]
# edges = [LEFT, RIGHT, BOTTOM, TOP]

# for i, edge in enumerate(edges):
#     clipped = clip_polygon(clipped, edge)
#     draw_polygon(t, clipped, colors[i], labels[i])
#     time.sleep(1)

# t.hideturtle()
# turtle.done()
