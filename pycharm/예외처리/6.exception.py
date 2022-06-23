
# 예외 처리 방식에서의 finally 옵션 구문 활용
def exception_test6(file_path):
    try:
        f = open(file_path, 'r')            # 파일 열기 시도
    except IOError:
        print('cannot open', file_path)     # 에러 메시지 출력
    else:
        print('File has', len(f.readlines()), 'lines')    # 파일 라인 수 출력
        f.close()                           # 파일 닫기
    finally:
        # 예외 발생 상관 없이 무조건 실행
        print('I just tried to read this file.', file_path)

# 정상 상황
exception_test6('README.txt')

# 없는 파일을 찾을때
exception_test6('README-XXX.txt')