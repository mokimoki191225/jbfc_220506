
import turtle as t

print('거북이를 키보드로 움직여 보아요')
print('\t A : 왼쪽으로 이동')
print('\t D : 오른쪽으로 이동')
print('\t W : 위쪽으로 이동')
print('\t S : 아래쪽으로 이동')
print('\t X : 종료')

input('엔터를 누르면 시작')
t.shape('turtle')
t.pensize(5)
t.color('blue')
t.speed(100)

while True:
    dir = input('[A,S,D,W] : ')
    if 'X'== dir.upper():
        break
    elif 'D'== dir.upper():
        t.setheading(45)
    elif 'W'== dir.upper():
        t.setheading(135)
    elif 'A'== dir.upper():
        t.setheading(225)
    elif 'S'== dir.upper():
        t.setheading(315)
    else :
        continue

    t.penup()
    t.forward(100)
    t.pendown()
    t.dot()

print('\n 프로그램 종료')
t.done()