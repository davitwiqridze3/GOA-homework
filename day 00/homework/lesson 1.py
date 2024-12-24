from turtle import *

#we want to paint a hous

#step 1:  draw a square

width(3)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)

forward(120)
right(90)

forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(200,200)
pendown()


left(30)
color("brown")
begin_fill()
forward(35)
right(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
end_fill()

penup()
goto(200,200)
pendown()
color("black")
left(180)
forward(200)
left(90)

forward(35)
color("brown")
begin_fill()
left(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
end_fill()














exitonclick()
