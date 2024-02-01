from turtle import *

#we want to paint house

#step 1:  draw a square
speed(1000000)
width(7)
color("purple")
forward(250) 
left(90)

forward(300)
left(90)

forward(250)
left(90)

forward(300)
left(90)
#end of square

#drawing a door

forward(100)
color("yellow")
begin_fill()
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(0, 300)
pendown()
color("red")
begin_fill()
left(140)
forward(210)
right(105)
forward(200)
end_fill()
color("brown")
penup()
goto(100, 180)
pendown()
begin_fill()
left(55.2)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
end_fill()
exitonclick()