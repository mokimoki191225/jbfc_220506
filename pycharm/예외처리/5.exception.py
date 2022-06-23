
# 예외 처리 방식에서의 else 옵션 구문 활용
def exception_test5(file_path):
    try:
        f = open(file_path, 'r')  # 파일 열기 시도
    except IOError:
        print('cannot open', file_path)  # 에러 메시지 출력
    else:
        print('File has', len(f.readlines()), 'lines')
        # 파일 라인 수 출력
        f.close()  # 파일 닫기

# 정상 상황
exception_test5('README.txt')

# 없는 파일을 찾을때
exception_test5('README-XXX.txt')