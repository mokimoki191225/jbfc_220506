
# 예외 클래스
class TooBigNumError(Exception):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return 'too big number {}. Use 1~10! '.format(self.val)

        # if 0<self.val<10:
        #     err_msg = '에러아님'
        # else:
        #     err_msg = 'too big number {}. Use 1~10! '.format(self.val)
        # return err_msg

print('프로그램 시작')
# raise TooBigNumError(5)
print('프로그램 종료')

# 사용자 정의 예외를 위한 테스트 함수
def user_defined_exception_test():
    num = int(input('1부터 10 사이의 점수를 입력하세요! : '))   # 숫자 입력
    if num > 10:
        raise TooBigNumError(num)                # 에러 발생
    print('숫자 {} 를 입력하셨군요! '.format(num))  # 정상인 경우 출력문

# 정상 Case 입력
# user_defined_exception_test()

# 에러 Case 입력
user_defined_exception_test()

# Traceback (most recent call last):
#   File "C:\project\basic_prog\day09\7.exception.py", line 30, in <module>
#     user_defined_exception_test()
#   File "C:\project\basic_prog\day09\7.exception.py", line 23, in user_defined_exception_test
#     raise TooBigNumError(num)                # 에러 발생
# __main__.TooBigNumError: too big number 11. Use 1~10!
