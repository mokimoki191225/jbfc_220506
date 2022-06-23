
def calculator(type,num1=0,num2=0):
    result=0
    if type == '+':
        result = num1+num2
    elif type == '-':
        result = num1-num2
    elif type == '*':
        result = num1*num2
    elif type == '/':
        result = int(num1/num2)
    else:
        print('잘못된기호입니다.!')
        result = 'Error!'
    return result

# def sum(num1,num2):
#     return num1+num2

result = calculator('+',10,8)
print(result)

result = calculator('-',10,8)
print(result)

result = calculator('*',10,8)
print(result)

result = calculator('/',10,8)
print(result)

num1=10
num2=9
type='-'
result=calculator(type,num1,num2)
print('값 : {}, {}, {}, 연산 : {}' .format(result,num1,num2,type))
