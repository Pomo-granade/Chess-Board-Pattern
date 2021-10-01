import turtle
t = turtle.Turtle()
t.speed(0)

def box(ln):
    for i in range(4):
        t.forward(ln)



y = 0

while True:
    t.goto(x, y)
    t.pendown()
    x += size
    t.begin_fill()
    if count % 2 == 0:
        t.color("black", "black")
    count += 1
    box(size)
    t.end_fill()
    if x >= size * 8:
        x = 0
        t.penup()
        y += size
        count += 1

