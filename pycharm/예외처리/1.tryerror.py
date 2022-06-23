
b = 0

try:

    print('안녕하세요?')
    # print(a)
    # if 1>0
    #     print('1은 0보다 크다.')
    print('이거 나오나?')

# Name error만 잡고 나머지는 넘긴다.
# if도 그렇고 작은 에러부터 써야 다음 넘어가는거 받는다.
# except NameError as err:
#     print('Name 에러발생')
#     print(err)

# SyntaxError error만 잡고 나머지는 넘긴다.
# if도 그렇고 작은 에러부터 써야 다음 넘어가는거 받는다.

# except IndentationError as err:
#     print('Syn 에러발생')
#     print(err)

# SyntaxError error만 잡고 나머지는 넘긴다.
# if도 그렇고 작은 에러부터 써야 다음 넘어가는거 받는다.

# except SyntaxError as err:
#     print('Syn 에러발생')
#     print(err)

# 대문자는 객체 클래스
except Exception as err:
    print('에러발생')
    print(err)

# finatlly 마무리하는 작업, close는 반드시 해야되기 때문에 이용한다.
finally:
    print('무조건 실행하는 코드')

# 예러가 아닌 경우 else로 뱉어낸다.
# else:
#     print('예외미발생')


