
#print
print('빨리 \n집에가고싶다.')
print("어여 퇴근(\'\' 혹은 \"\")합시다.")
print('어여 퇴근(\'김영목\' 혹은 \"\")합시다.')
mok = 'good'
print(mok)

# 숫자 출력
print(100)
print(150 + 200)
print(150 - 200)

# 기본연산
x = 50
y = 4.
print("x = ", x)
print("y = ", y)
print("x + y = " , x+y)
print("x - y = " , x-y)
print("x * y = " , x*y)
print("x / y = " , x/y)
print("x //y = " , x//y)
print("x % y = " , x%y)
print("-x = "    , -x)
print("+x = "    , +x)
print("x ** y = ", x**y)
print("pow(x,y) = ", pow(x,y))

a = '김영목'
b = '퇴근'

print(a,b)

text = a + '님,' + b +'하세요'
print(text)

#input

a = 10
b = 10

print('%s님,%s하세요'%(a,b))
print('{}님,{}하세요'.format(a,b))

#input('이름을 입력하세요.')
my_name = input('이름을 입력하세요.')
print('나의 이름은', my_name, '입니다.')


# 변수에 숫자담기

coffee1_name = '바보';  coffee1_val = 10;
coffee2_name = '멍충이';  coffee2_val = 20;

print('너는' + coffee1_name + coffee2_name + '입니다.')
print('IQ는 ' + str(coffee1_val + coffee2_val) + '입니다.')

IQ=coffee1_val + coffee2_val
print('너는, \n        %s, %s 입니다.' % (coffee1_name, coffee2_name))
print('IQ는        %d 입니다.' %IQ)

name = input('니 이름이 모니?')
print(name + '인데요? 왜요?')
order = input('커피 묵을래? \n모 묵을래?')
count = input('몇잔 묵을래?')
print('%s %s잔을 주문하셨습니다. \n잠시만 기다려주세요~^^' % (order, count))
price = 5000
cost = price * int(count)
print('%s %s잔을 주문하셨습니다. \n결재하실 금액은 %d원입니다~^^' % (order, count, cost))

import turtle

input('엔터를 치면 거북이 등장.')
turtle.shape('turtle')
turtle.color('red')
turtle.pensize(10)
turtle.circle(100)

input('엔터를 치면 앞으로 전집합니다.')
turtle.forward(100)

input('엔터를 치면 왼쪽으로 전집합니다.')
turtle.left(90)
turtle.forward(100)

input('엔터를 치면 오른쪽으로 전집합니다.')
# turtle.sleep(1)
turtle.right(90)
turtle.forward(50)

turtle.done()


#for문
for x in range(3):
    print(x,x+5)

for x in range(10):
    print(x,x-5)
