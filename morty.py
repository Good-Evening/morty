import turtle
import os

wn = turtle.Screen()
jeff = turtle.Turtle()

wn.addshape(os.path.expanduser("morty.gif"))
jeff.shape(os.path.expanduser("morty.gif"))
wn.bgcolor("#000000")

#draws the image
jeff.penup()
jeff.goto(350, 0)
jeff.stamp()

#sets up jeff's properties
jeff.pensize(4)
jeff.shape("arrow")
jeff.color("white")
jeff.speed(100)
jeff.tracer(20)
jeff.goto(-385, 375)
jeff.write("Jeffrey Darren Wang")
jeff.color("black")

#draws hair
jeff.fillcolor("#8b5b2f")
jeff.goto(-150, 175)
jeff.pendown()
jeff.setheading(80)
jeff.begin_fill()
for i in range(30):
    jeff.forward(4)
    jeff.left(2)
for i in range(15):
    jeff.forward(2)
    jeff.right(1)
for i in range(40):
    jeff.forward(2)
    jeff.left(1)
for i in range(15):
    jeff.forward(5)
    jeff.left(1)
for i in range(20):
    jeff.forward(2)
    jeff.left(1)
for i in range(10):
    jeff.forward(1)
    jeff.right(1)
jeff.forward(50)
for i in range(10):
    jeff.forward(2)
    jeff.right(1)
for i in range(30):
    jeff.forward(4)
    jeff.left(2)
for i in range(10):
    jeff.forward(1)
    jeff.left(1)
for i in range(20):
    jeff.forward(1)
    jeff.right(1)
for i in range(20):
    jeff.forward(3)
    jeff.left(1)
for i in range(30):
    jeff.forward(4)
    jeff.left(1)
for i in range(20):
    jeff.forward(3)
    jeff.right(1)
for i in range(20):
    jeff.forward(2)
    jeff.left(1)
for i in range(25):
    jeff.forward(1)
    jeff.left(1)
for i in range(10):
    jeff.forward(1)
    jeff.right(2)
for i in range(20):
    jeff.forward(3)
    jeff.left(3)
jeff.end_fill()
jeff.penup()
#finally done with the hair :D

jeff.tracer(1)
#draws shirt/body
jeff.goto(-410, -100)
jeff.setheading(215)
jeff.fillcolor("#e6ec8b")
jeff.pendown()
jeff.begin_fill()
for i in range(15):
    jeff.forward(10)
    jeff.left(2)
for i in range(17):
    jeff.forward(13)
    jeff.left(1)
jeff.penup()
jeff.goto(-170, -425)
jeff.setheading(95)
jeff.pendown()
for i in range(23):
    jeff.forward(15)
    jeff.left(1)
jeff.end_fill()
jeff.penup()
jeff.goto(-465, -375)
jeff.setheading(255)
jeff.pendown()
for i in range(3):
    jeff.forward(15)
    jeff.left(1)
jeff.penup()
jeff.goto(-230, -330)
jeff.setheading(275)
jeff.pendown()
for i in range(6):
    jeff.forward(15)
    jeff.right(1)
jeff.penup()

jeff.tracer(20)
#draws head
jeff.fillcolor("#ffdbbe")
jeff.goto(-350, -200)
jeff.pendown()
jeff.begin_fill()
jeff.setheading(0)
for i in range(60):
    jeff.forward(25)
    jeff.left(6)
jeff.end_fill()

#draws the ear
jeff.penup()
jeff.goto(-510, -100)
jeff.left(200)
jeff.pendown()
jeff.begin_fill()
for i in range(38):
    jeff.forward(4)
    jeff.right(5)
jeff.end_fill()

#draws the eyebrows
jeff.speed(100)
jeff.penup()
jeff.goto(-455, 160)
jeff.left(30)
jeff.pendown()
    #left eyebrow
for i in range(25):
    jeff.forward(4)
    jeff.right(1)
jeff.penup()
jeff.setheading(0)
jeff.forward(165)
jeff.pendown()
    #right eyebrow
for i in range(10):
    jeff.forward(4)
    jeff.right(2)

#draws eyes
jeff.setheading(0)
jeff.fillcolor("#fcfcfc")
jeff.penup()
jeff.goto(-360, 0)
jeff.pendown()
    #draws left eye
jeff.begin_fill()
for i in range(36):
    jeff.forward(14)
    jeff.left(10)
jeff.end_fill()
    #draws right eye
jeff.penup()
jeff.goto(-160, 15)
jeff.pendown()
jeff.begin_fill()
for i in range(36):
    jeff.forward(13)
    jeff.left(10)
jeff.end_fill()
    #draws left pupil
jeff.penup()
jeff.goto(-335, 110)
jeff.pendown()
for i in range(10):
    jeff.forward(7)
    jeff.backward(7)
    jeff.left(36)
    #draws left pupil
jeff.penup()
jeff.goto(-160, 120)
jeff.pendown()
for i in range(10):
    jeff.forward(7)
    jeff.backward(7)
    jeff.left(36)

#draws nose
jeff.penup()
jeff.goto(-230, 25)
jeff.pendown()
jeff.right(35)
jeff.forward(20)
for i in range (55):
    jeff.forward(1)
    jeff.right(3)
jeff.forward(20)

#draws mouth
jeff.setheading(275)
jeff.penup()
jeff.goto(-230, -55)
jeff.pendown()
    #draws upperlip
jeff.forward(35)
jeff.right(5)
for i in range (3):
    jeff.forward(8)
    jeff.right(4)
for i in range(23):
    jeff.forward(1)
    jeff.right(6)
for i in range(4):
    jeff.forward(5)
    jeff.right(10)
    #draws lowerlip
jeff.setheading(270)
for i in range(4):
    jeff.forward(8)
    jeff.right(6)
for i in range(10):
    jeff.forward(2)
    jeff.right(12)
for i in range(5):
    jeff.forward(4)
    jeff.right(7)
jeff.forward(10)

#locates turtle elsewhere
jeff.penup()
jeff.goto(500,500)
jeff.pendown()

# this helps ensure that tracer will draw everything
for i in range(20):
    jeff.right(18)

wn.exitonclick()