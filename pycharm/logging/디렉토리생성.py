import os

newfloder = input('디렉터리명을 입력하세요')

# 오류날때 예외처리하기

try:
    os.mkdir(newfloder)
    print('[%s] 디렉터리 생성' %(newfloder))
except Exception as e:
    print(e)