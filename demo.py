import turtle
t=turtle.Turtle()
t.speed(150)
turtle.bgcolor('black')
for i in range(250):
    t.color('green')
    t.circle(i)
    t.left(5)
    turtle.done()