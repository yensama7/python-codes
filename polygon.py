from turtle import *

draw = Turtle()
draw.penup()
draw.goto(-100,100)
draw.pendown()

def shape_draw(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        draw.forward(100)
        draw.right(angle)

    

for num_sides in range(3,11):
    shape_draw(num_sides)