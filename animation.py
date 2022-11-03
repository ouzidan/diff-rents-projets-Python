
import turtle

turtle.speed(0)
turtle.bgcolor("black")
turtle.hideturtle()
Colors =["yellow","green","blue","red"]

for i in range(500):
    for c in Colors:
        turtle.color(c)
        turtle.forward(i)
        turtle.left(2222)
        turtle.tracer(10111)


turtle.mainloop()
