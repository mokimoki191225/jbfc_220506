
import turtle as t

def tun_right():
    t.setheading(0)
    t.forward(10)

def tun_up():
    t.setheading(90)
    t.forward(10)

def tun_down():
    t.setheading(270)
    t.forward(10)

def tun_left():
    t.setheading(180)
    t.forward(10)

def blank():
    t.clear()

t.shape('turtle')
t.speed(10)
t.onkeypress(tun_right,"Right") #onkeypress는 뒤에 문자가 대문자 인식해야한다.
t.onkeypress(tun_up,"Up")
t.onkeypress(tun_down,"Down")
t.onkeypress(tun_left,"Left")
t.onkeypress(blank,"Escape")
t.listen() #키 눌렀졌을때 계속 인식 실행
t.mainloop()

#마우스

import turtle as t
t.speed(1)
t.pensize(5)
t.shape('turtle')
t.onscreenclick(t.goto)
t.mainloop()
