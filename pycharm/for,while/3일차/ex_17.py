# 복합패턴 반복문

import turtle

turtle.color("red")
turtle.pensize(1)

# 각도, 길이, 굵기, 색상
angle = 45
length = 1
thick = 1
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'cyan', 'magenta', 'violet']

# while x < 8:
for i in range(1, 45):
length = i*5
thick = i

turtle.left(angle)
turtle.forward(length)
turtle.pensize(thick)
turtle.color(colors[i % 8])

turtle.done()

