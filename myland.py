import turtle


scn = turtle.Screen()
geras = turtle.Turtle()
geras2 = turtle.Turtle()
flawer = turtle.Turtle()
haws = turtle.Turtle()
sky = turtle.Turtle()
haws = turtle.Turtle()

geras.speed(.5)
geras2.speed(.5)
flawer.speed(.5)
haws.speed(.5)
sky.speed(.5)
haws.speed(.5)

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

def flawers():
    flawer.color("Goldenrod")
    flawer.penup()
    flawer.right(90)
    flawer.forward(90)
    flawer.right(90)
    flawer.forward(80)
    flawer.right(180)
    flawer.pendown()
    flawer.pensize(7)
    flawer.right(-90)
    flawer.forward(60)
    flawer.right(90)
    flawer.pensize(1)
    flawer.color("Chartreuse")
    for i in range(15):
        flawer.begin_fill()
        for i in range(4):
            flawer.forward(20)
            flawer.right(-90)
        flawer.right(24)
        flawer.end_fill()
    flawer.color("Indian Red")
    flawer.right(90)
    flawer.forward(20)
    flawer.right(270)
    flawer.begin_fill()
    flawer.circle(20)
    flawer.end_fill()
    flawer.right(-90)
    flawer.forward(20)


def Haws():
    haws.begin_fill()
    haws.color("Medium Violet Red")
    haws.forward(230)
    haws.right(-90)
    haws.forward(110)
    haws.right(-90)
    haws.forward(230)
    haws.end_fill()
    haws.begin_fill()
    haws.color("Red")
    haws.forward(100)
    haws.right(-90)
    haws.forward(110)
    haws.right(-90)
    haws.forward(100)
    haws.end_fill()
    haws.color("Medium Violet Red")
    haws.right(-90)
    haws.forward(110)
    haws.right(-45)
    haws.forward(70)




Haws()
gera()
flawers()
flawer.penup()
flawer.goto(190, 0)
flawer.right(90)
flawers()



turtle.exitonclick()


