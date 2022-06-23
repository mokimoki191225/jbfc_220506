
#과제 for 혹은 while 사용하여 그려보기

#육각형그리기

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

#돌리기

import turtle as t

num_circle = 30
radius = 180

t.bgcolor('red')
t.color('blue')
t.speed(3000)

for _ in range(num_circle): #_는 의미없는 값이다.
    t.circle(radius)
    t.left(360/num_circle)

t.done()


