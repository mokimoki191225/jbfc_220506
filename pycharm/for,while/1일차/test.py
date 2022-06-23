
for x in range(3):
    print(x,x+5)

for x in range(10):
    print(x,x-5)

import turtle

input('엔터를 치면 거북이 등장.')
turtle.shape('turtle')
turtle.color('red')
turtle.pensize(10)
# turtle.circle(100)

input('엔터를 치면 앞으로 전집합니다.')
turtle.forward(100)

input('엔터를 치면 왼쪽으로 전집합니다.')
turtle.left(120)
turtle.forward(100)

input('엔터를 치면 오른쪽으로 전집합니다.')
turtle.left(120)
turtle.forward(100)

turtle.done()
    

