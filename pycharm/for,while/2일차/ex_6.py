
# Immutable (바꿀수없는) 예제
hello = '뭐라는교?'

print(hello)
print(id(hello))

hello = '반삽습니다.?'

print(hello)
print(id(hello))

# mutable (바꿀수있는) 예제, run타임 오류시 쉽게 찾을 수 있다

hello_list = ['뭐라는교?']

print(hello_list)
print(id(hello_list))

hello_list[0] = '반삽습니다.?' # 0은 덩어리이다
# hello_list = ['반삽습니다.?']

print(hello_list)
print(id(hello_list))



