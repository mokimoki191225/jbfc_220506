
import turtle

t=turtle.Turtle()
t.shape('turtle')

dot_distance = 30
width = 100
height = 100

t.penup()
for y in range(height):
    for i in range(width):
        t.dot()
        t.forward(dot_distance)

    t.backward(dot_distance*width)
    t.right(90)
    t.forward(dot_distance)
    t.left(90)

turtle.done()