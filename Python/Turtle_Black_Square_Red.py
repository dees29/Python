import turtle
t=turtle.Turtle()
t.color("white")
wn=turtle.Screen()
wn.bgcolor("black")
t.speed(1)
t.begin_fill()
t.fillcolor("red")
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
t.hideturtle()
