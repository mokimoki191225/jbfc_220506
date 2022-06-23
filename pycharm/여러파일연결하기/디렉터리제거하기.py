
#디렉터리 제거하기(osrmdir)

import os

#target_folder = newfolder

target_folder = "aaa"

k = input('[%s] 디렉터리를 삭세하시겠습니까? (y/n)' %target_folder)
if k == 'y':
    try:
        os.rmdir(target_folder)
        print('[%s] 디렉터리를 삭제했습니다.' %target_folder)
    except Exception as e:
        print(e)