from turtle import *

#we want to paint GOA logo

#step: 1 draw background
bgcolor("black")
speed(20)

color("grey")

#drawing horizontal lines
def lines(x,y):
    penup()
    goto(x,y)
    pendown()
    forward(1600)

lines(-800, 300)
lines(-800, 200)
lines(-800, 100)
lines(-800, 0)
lines(-800, -100)
lines(-800, -200)
lines(-800, -300)

#drawing vertical lines
def lines(x,y):
    penup()
    goto(x,y)
    pendown()
    goto(x, y - 800)


lines(-800, 400)
lines(-700, 400)
lines(-600, 400)
lines(-500, 400)
lines(-400, 400)
lines(-300, 400)
lines(-200, 400)
lines(-100, 400)
lines(0, 400)
lines(100, 400)
lines(200, 400)
lines(300, 400)
lines(400, 400)
lines(500, 400)
lines(600, 400)
lines(700, 400)
lines(800, 400)


#making GOA logo
def squares(x,y):
    penup()
    goto(x,y)
    pendown()

    color("white")
    begin_fill()
    forward(40)
    left(90)
    forward(40)
    left(90) 
    forward(40)
    left(90)
    forward(40)
    left(90)
    end_fill()





squares(-500,-100)
squares(-500, -40)
squares(-500, 20)
squares(-500, 80)
squares(-500, 140)
squares(-440, 140)
squares(-380, 140)
squares(-320, 140)
squares(-440, -100)
squares(-380, -100)
squares(-320, -100)
squares(-320, -40)
squares(-320, 20)
squares(-380, 20)




def square(x,y):
    penup()
    goto(x,y)
    pendown()

    color("green")
    begin_fill()
    forward(260)
    left(90)
    forward(280)
    left(90) 
    forward(260)
    left(90)
    forward(280)
    left(90)
    end_fill()

square(-190, -100)


def square(x,y):
    penup()
    goto(x,y)
    pendown()

    color("black")
    begin_fill()
    forward(160)
    left(90)
    forward(180)
    left(90) 
    forward(160)
    left(90)
    forward(180)
    left(90)
    end_fill()

square(-140,-50)



def squares(x,y):
    penup()
    goto(x,y)
    pendown()

    color("white")
    begin_fill()
    forward(40)
    left(90)
    forward(40)
    left(90) 
    forward(40)
    left(90)
    forward(40)
    left(90)
    end_fill()

squares(100,-100)
squares(140, -40)
squares(180, 20)
squares(220, 80)
squares(260, 140)
squares(260, 20)

penup()
goto(300,180)
pendown()
begin_fill()
forward(40)
left(270)
forward(280)
left(270)
forward(40)
left(270)
forward(280)
end_fill()














exitonclick()





































