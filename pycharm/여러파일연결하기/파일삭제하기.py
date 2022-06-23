
# 파일삭제하기(osremove)

import os

target_file = './data/mydata_copy.txt'
k = input('[%s] 파일을 삭제하시겠습니까? ([y]/n)' %(target_file))

if k=='y' or k=='':
    os.remove(target_file)
    print('[%s] 파일을 삭제했습니다.' %target_file)