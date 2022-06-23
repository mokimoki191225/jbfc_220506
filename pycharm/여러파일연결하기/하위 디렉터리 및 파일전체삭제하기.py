
# 하위 디렉터리 및 파일 전체 삭제하기(shutil.rmtree)

import shutil
import os

target_floder = "./aaa"

print('[%s] 하위 모든 디렉터리 및 파일들을 삭제합니다.' %target_floder)

for file in os.listdir(target_floder):
    print(file)
k = input('[%s]를 삭제하겠습니까? (y/n)' %target_floder)

if k=='y':
    try:
        shutil.rmtree(target_floder)
        print('[%s]의 모든 하위 디렉터리와 파일들을 삭제했습니다.' %target_floder)
    except Exception as e:
        print(e)
