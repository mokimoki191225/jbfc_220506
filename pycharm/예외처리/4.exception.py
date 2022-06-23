

import traceback

# 예외상황에 대한 처리를 구현한 함수
def exception_test4():
    print("[1] Can you add 2 and '2' in python? ")

    try:
        print("[2] Try it~! ", 2 + '2')  # TypeError 발생

    except TypeError:
        print('[2] 타입에러')
        traceback.print_exc()
        #트레이스백 메시지 출력
        #앞에 함수들을 간단하게 출력하는 함수

    print('[3] 추가하는것 가능하냐?')

exception_test4()