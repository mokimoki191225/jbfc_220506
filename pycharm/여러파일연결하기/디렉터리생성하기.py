
#디렉터리 생성하기(osmkdir)

import os

newfolder = input('새로 생성할 디렉터리 이름을 입력하세요.')

#오류 처리날때 예외로 처리하기
try:
    os.mkdir(newfolder)
    print('[%s] 디렉터리를 새로 생성했습니다.' %newfolder)
except Exception as e:
    print(e)