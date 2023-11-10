# a requirement for this game is the turtle module
# use py -m pip install turtle on windows
# use python3 -m pip install turtle on mac
# up - w
# down - s
# left - a
# right - d

import turtle
import time
import random

delay = 0.1

#score
score = 0
high_score = 0

#screen setup****************************************
window = turtle.Screen()
window.title("snake game by yensama7")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0)

#snake head******************************************
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"
#***************************************************

#food***********************************************
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
#***************************************************
segments = []

#score**********************************************
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Score: 0  High Score: 0", align ="center", font=("courier", 24, "normal"))


# movement functions********************************
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"
    

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#keyboard bindings*********************************
window.listen()
window.onkeypress(go_up,"w")
window.onkeypress(go_down,"s")
window.onkeypress(go_left,"a")
window.onkeypress(go_right,"d")


#main game loop*************************************
while True:
    window.update()

    #checks for collision with border*******************
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide segments
        for segment in segments :
            segment.goto(1000,1000)

        #clear segments
        segments.clear()

        #reset score
        score = 0
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align ="center", font=("courier", 24, "normal"))
        #reset delay 
        delay = 0.1


    #checks for collision with food*******************
    if head.distance(food) < 20:
        #moves food to a new position
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #add segments
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)
        #********************************************

        #shorten delay 
        delay -= 0.001

        #score increment
        score += 10
        if score > high_score:
            high_score = score
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align ="center", font=("courier", 24, "normal"))
            

    #collision with body
    for i in segments:
        if head.distance(i) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for s in segments:
                s.goto(1000,1000)

            segments.clear()

            #reset score
            score = 0
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align ="center", font=("courier", 24, "normal"))

            #reset delay 
            delay = 0.1
            

    #segments move at each other backs
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #moves at the first head's back
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
            

    
    move()

    time.sleep(delay)

window.mainloop()
#****************************************************
