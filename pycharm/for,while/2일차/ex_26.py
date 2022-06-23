
import turtle

in_color = input('원의색깔(R/G/B/etc)')
in_filled = input('원의색깔(Yes/No)')

if in_color == 'R' or in_color == 'r':
    color='red'
elif in_color == 'G' or in_color == 'g':
    color='green'
elif in_color == 'B' or in_color == 'b':
    color='blue'
else:
    color='black'

turtle.begin_fill() #채우기 시작하라

turtle.color(color)
turtle.pensize(10)
turtle.circle(100)

if in_filled=='Y' or in_filled=='y':
    turtle.end_fill() #채우기 끝내라
else:
    pass

turtle.done()