
#도형그리기

import turtle
import math

width = 200
root = math.sqrt(width**2+width**2)

input('엔터를 치면 거북이 등장.')
turtle.shape('turtle')
turtle.color('blue')
turtle.pensize(10)

input('엔터를 치면 앞으로 전집합니다.')
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(135)
turtle.forward(root)
turtle.left(135)
turtle.forward(200)
turtle.left(135)
turtle.forward(root)
turtle.left(135)
turtle.forward(200)
turtle.left(45)
turtle.forward(root/2)
turtle.left(90)
turtle.forward(root/2)

turtle.done()

