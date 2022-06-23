# 이스케이프 문자

test='파이썬 프로그래밍 재미있다!'

result = test.startswith('파이썬')
print(result)

result = test.endswith('!')
print(result)

result = test.endswith('어려워요!')
print(result)

result = test.replace('파이썬', 'Python')
print(result)

print('test') # Shift + Enter은 줄만 띄는 거다.

test = 'Pytion is Interesting'

result = test.upper()
print(result)

result = test.lower() #.을 붙이는 것이 무엇인가?
print(result)

'''
result = '/'.lower(test) 
print(result)
'''

result = '/'.join(test)
print(result)

print(result.islower())
print(result.isupper())






