
from Packages import is_num_

idx,num,gop = 0,0,0
total_sum = []
factorial = []

a = input('숫자를 입력해주세요 => ')
print(is_num_.is_num(a))
print('-'*50)
# print(type(a))
numbers = list(range(int(a)+1))
# print(numbers)

while idx < len(numbers):
    num = numbers[idx]
    gop = gop * num
    gop=1 if gop<1 else gop
    factorial.append(gop)
    idx = idx+1

print('팩토리얼 테이블입니다.')
print('-'*50)

def cs_num(num):
    ret_num = str()
    str_num = str(num)
    rev_num = str_num[::-1]
    tmp_num = str()

    for i in range(len(rev_num)): #3자리
        if (i>0) and (i%3==0):
            tmp_num = tmp_num + ','
        tmp_num = tmp_num + rev_num[i]

    ret_num = tmp_num[::-1]
    return ret_num

# print(cs_num(123456789))

# 함수 활용안하고 자체적으로
# for fact_num in range(len(factorial)):
#     print('{}! = {:,}' .format(fact_num, factorial[fact_num]))

# 함수 활용
for fact_num in range(len(factorial)):
    print('{}! = {}' .format(fact_num, cs_num(factorial[fact_num])))





