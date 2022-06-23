
import turtle

# turtle.shape('turtle')
input('엔터를 치면 거북이 등장.')
turtle.shape('turtle')

size  = input('사각형크기 100 ~ 300 ')
color = input('색깔') #띄어쓰기 색깔입력은 오류 뱉어낸다.
thick = input('굵기') #숫자는 띄어쓰기해도 상관없다.

angle = 90
thick = int(thick)
size = int(size)

turtle.color(color)
turtle.pensize(thick)

turtle.left(angle)
turtle.forward(size)

turtle.right(angle)
turtle.forward(size)

turtle.right(angle)
turtle.forward(size)

turtle.right(angle)
turtle.forward(size)

turtle.done()

