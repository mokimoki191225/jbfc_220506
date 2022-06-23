
# 디렉터리 생성하기 (osmkdir)
# 비쥬얼 스튜디오, 아톰

import os

newfloder = input('디렉터리명을 입력하세요')

# 오류날때 예외처리하기

try:
    os.mkdir(newfloder)
    print('[%s] 디렉터리 생성' %(newfloder))
except Exception as e:
    print(e)

# 파일이름 바꾸기(osrename)

# from os import rename
#
# folder_path = "./data"
# target_file = folder_path + 'mydata.txt'
# newname = input('[%s]에 대한 새로운 파일 이름을 입력하세요.' %(target_file))

# new_file = folder_path + rename

# new_file = newname
# rename(target_file,new_file)
# print('[%s] -> [%s]로 파일이름이 변경되었습니다.' %(target_file, new_file))




