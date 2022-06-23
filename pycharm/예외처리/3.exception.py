
# 예외상황 테스트를 위한 함수
# def exception_test():
#     print("[1] Can you add 2 and '2' in python? ")
#     print("[2] Try it~! ", 2 + '2')  # 예외 발생
#     print("[3] It's not possible to add integer and string together. ")
#
#
# exception_test()


# 예외상황에 대한 처리를 구현한 함수
# def exception_test2():
#     print("[1] Can you add 2 and '2' in python? ")
#
#     try:
#         print("[2] Try it~! ", 2 + '2')  # TypeError 발생
#     except TypeError:
#         print("[2] I got TypeError! ")  # 에러 메시지 출력
#
#     print("[3] It's not possible to add integer and string together. ")
#
#
# exception_test2()

# 예외상황에 대한 처리를 구현한 함수
# def exception_test2():
#     print("[1] Can you add 2 and '2' in python? ")
#
#     try:
#         print("[2] Try it~! ", 2 + '2')  # TypeError 발생
#
#     except Exception as err:
#         print('[e1]', err.__str__())
#         print('[e2]', err.__class__)
#         print('[e3]', err.__dict__)
#         print('='*100)
#         err_msg = '{} :: {}'.format(err.__class__, err)
#         print('Log 파일에 저장되는 부분 : {}'.format(err_msg))  # 에러 메시지 출력
#
# exception_test2()

from datetime import datetime

module_name = 'FileName'

# 예외상황에 대한 처리를 구현한 함수
def exception_test2():
    method_name = 'exception_test2()'
    print("[1] Can you add 2 and '2' in python? ")

    try:
        print("[2] Try it~! ", 2 + '2')  # TypeError 발생

    except Exception as err:
        print('[e1]', err.__str__())
        print('[e2]', err.__class__)
        print('[e3]', err.__dict__)
        print('='*100)
        current_time = datetime.now()
        log_time = 'cur_time : {}'.format(str(current_time)[:19])
        # print(log_time)
        #10의 -6승까지 찍혀있다.
        # print('cur_time:',current_time)
        err_msg = '\n {} {}. {} 에러 발생  \n{} :: {}'.format(log_time, module_name, method_name, err.__class__, err)
        print('Log 파일에 저장되는 부분 : {}'.format(err_msg))  # 에러 메시지 출력

exception_test2()