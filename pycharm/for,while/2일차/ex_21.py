
#조건연산

condition = False

if condition:
    print('사실이야')
else:
    print('거짓이야')

a=200
b=100
max=0

if a>b:
    print('a가 더커')
    max = a
elif a<b:
    print('b가 더커')
    max = b
else:
    print('같애')
    max = b

print('a와b중 최대값은', max, '입니다.')

