import turtle
t=turtle.Turtle()
t.color("white")
wn=turtle.Screen()
wn.bgcolor("black")
t.speed(1)
t.begin_fill()
t.fillcolor("red")
t.circle(100,steps=8)
t.end_fill()
t.hideturtle()
