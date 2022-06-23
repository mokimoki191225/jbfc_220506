
def add_txt(arg1,arg2):
    print(arg1,arg2)

parma1='가'
parma2='나'

add_txt(parma1,parma2)

def add_num(num1,num2):
    result = num1+num2
    return result

parma1 = 40
parma2 = 50

sum = add_num(parma1,parma2)
print('%d와 %d의 합은 %d입니다.' %(parma1,parma2,sum))