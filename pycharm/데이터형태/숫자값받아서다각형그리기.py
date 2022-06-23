
import turtle

var1 = int(input('각형?',)) #각형
var2 = int(input('변의길이?',)) #변의수

print(type(var1))

angle = 360.0 / var1
colors = var1 % 3
color = 'red' if colors==0 else 'green' if colors==1 else 'blue'

turtle.begin_fill()
turtle.color(color)
turtle.pensize(10)

for x in range(var1):
    turtle.forward(var2)
    turtle.left(angle)

turtle.end_fill()

turtle.done()





