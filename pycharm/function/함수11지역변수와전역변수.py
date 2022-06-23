
#지역변수와 전역변수

param=10
st='저녁변수'

def fun1():
    st='지역변수'
    print('fun.st = %s, id=%d' %(st,id(st)))
print('*'*20)
fun1()
print('fun.st = %s, id=%d' %(st,id(st)))

def fun2(param):
    param=20
    print('fun.st = %s, id=%d' %(param,id(param)))
print('*'*20)
fun2(param)
print('fun.st = %s, id=%d' %(param,id(param)))

def fun3():
    global param #저녁변수
    print('fun.st = %s, id=%d' %(param,id(param)))
print('*'*20)
fun3()
print('fun.st = %s, id=%d' %(param,id(param)))
