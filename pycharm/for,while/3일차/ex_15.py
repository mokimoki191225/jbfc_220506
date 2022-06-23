
#구구단 출력하기

a = input('출력할 단수 입력 [2~9]', )
b = list(range(1,10))

print('*'*50)

for y in b:
    print('%s * %s = ' %(a,y),end='')
    print(int(a)*int(y))
else: pass

c = len(b)
print(b)
print(c)