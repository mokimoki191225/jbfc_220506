
#야구게임
# 답 : 123
# 불 : 567--->
# 불 : 367---> 1B
# 불 : 167---> 1S

# 3자리 불러오기
# import random
#
# def randomthree():
#     numbers=[]
#
#     while len(numbers) <3:
#         num=random.randint(0,9)
#         if num not in numbers:
#             numbers.append(num)
#     print('0과 9사이의 서로 다른 숫자3개를 랜덤한 순서로 뽑자')
#     return numbers
#
# print(randomthree())
# e=randomthree()
# print(type(randomthree()))

# 3자리 불른다 내가

# x = [4,5,6]
#
# def randomna(a,b,c):
#     d=[a,b,c]
#     return d
#
# a=5
# b=6
# c=7
# d=[a,b,c]
# print(x)
# print(randomna(*d))

# 스트라이크 볼 부른다.

# strike=0
# ball=0

# for i in range(3):
#     if d[i] == x[i]:
#         strike=strike+1
#         print(strike)
#     elif d[i] in x:
#         ball = ball + 1
# print(strike,ball)

import random

def randomthree():
    numbers=[]

    while len(numbers) <3:
        num=random.randint(0,9)
        if num not in numbers:
            numbers.append(num)
    print('0과 9사이의 서로 다른 숫자3개를 랜덤한 순서로 뽑자')
    return numbers

x=randomthree()
print('난수 {}'.format(x))

# x = [4,5,6]
#난수

def randomna(a,b,c):
    d=[a,b,c]
    return d #불른 숫자 만들기

strike=0
ball=0

# print(x)

while True:
    a=int(input('첫자리 또 불러봐'))
    b=int(input('둘자리 또 불러봐'))
    c=int(input('세자리 또 불러봐'))
    d=randomna(a,b,c)
    print(d)
    for i in range(3):
        if d[i] == x[i]:
            strike = strike + 1
        elif d[i] in x:
            ball = ball + 1
    print('%d 스트라이크, %d 볼' %(strike, ball))
    if d==x:
        print('성공')
        break
    else:
        continue

# d=input('또 불러봐')













# def a():
#     b=[]
#     while len(b)<3:
#         c=

