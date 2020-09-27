import turtle
t=turtle.Turtle()
list1=["yellow","red","blue","green"]
t.up()
t.goto(200,0)
for i in range(4):
    t.down()
    t.pensize(20)
    t.color(list1[i])
    t.circle(100)
    
    t.up()
    t.bk(100)
    t.down()
