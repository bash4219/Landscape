import turtle


scn = turtle.Screen()
geras = turtle.Turtle()
geras2 = turtle.Turtle()
sky = turtle.Turtle()
haws = turtle.Turtle()

def gera():
    geras.color("green")
    geras.begin_fill()
    geras.forward(1500)
    geras.right(90)
    geras.forward(1500)
    geras.right(90)
    geras.forward(1500)
    geras.end_fill()
    geras2.color("green")
    geras2.begin_fill()
    geras2.right(180)
    geras2.forward(1500)
    geras2.right(-90)
    geras2.forward(1500)
    geras2.right(-90)
    geras2.forward(1500)
    geras2.end_fill()
    geras2.goto(0, 0)
    geras.goto(0, 0)


gera()


turtle.exitonclick()


