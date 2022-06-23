
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


