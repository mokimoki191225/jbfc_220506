
idx, gop, sum = 0,0,0
factorial = []
total_sum = []

num_chk_list = list('0123456789')

print(num_chk_list)

while True :
    key_in = input('숫자 입력=>')
    chk_num = True
    for char in key_in:
        is_num = char in num_chk_list
        chk_num=chk_num*is_num
        if not is_num:
            break
    if chk_num:
        last_num = int(key_in)
        print('입력숫자',last_num)
        break
    else:
        print('입력숫자아님')

#입력값이 숫자인 경우, 미션 수행

title= str(last_num) + '까지의 합계'
print(title)

numbers = list(range(last_num+1))

while idx < len(numbers) :
    num = numbers[idx]
    sum=sum+num
    gop=gop*num
    gop = 1 if gop<1 else gop

    total_sum.append(sum)
    factorial.append(gop)
    idx+=1

print(last_num,'까지 합계는', total_sum[-1],'입니다')
print('아래는 팩토리얼')

for fact_num in range(len(factorial)):
    print(str(fact_num),factorial[fact_num])
