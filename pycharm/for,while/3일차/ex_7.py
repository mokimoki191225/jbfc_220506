
#pass, break, continue

ex= list(range(1,1000))

for num in ex:
    if num <=5:
        if num%2==0:
            pass
            print(num,'짝수입니다.')
        else:
            continue
            print(num,'홀수입니다.') #뱉어내지 않고 다시 if로 실행한다. 찍히지 않는다.
    else:
        print(num,'큰수입니다')
        break
        print('브레이크') #전체를 탈출한다.

print('종료')



