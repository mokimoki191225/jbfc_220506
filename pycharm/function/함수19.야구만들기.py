
#1. 야구 정답 만들기
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

#2. 부르는 숫자 만들기

def randomna(a,b,c):
    d=[a,b,c]
    return d #불른 숫자 만들기

strike=0
ball=0

#3. 비교하는 야구게임

t_cnt = 0
while True:
    t_cnt += 1
    # a=int(input('첫자리 또 불러봐'))
    # b=int(input('둘자리 또 불러봐'))
    # c=int(input('세자리 또 불러봐'))
    u_num = input("3자리 숫자입력 : ")
    a = int(u_num[0])
    b = int(u_num[1])
    c = int(u_num[2])

    d=randomna(a,b,c)
    print(d)
    for i in range(3):
        if d[i] == x[i]:
            strike = strike + 1
        elif d[i] in x:
            ball = ball + 1

    print("{}번째 :".format(t_cnt), end="\t")
    print('%d 스트라이크, %d 볼' %(strike, ball))
    if d==x:
        print('성공')
        break
    else:
        continue
