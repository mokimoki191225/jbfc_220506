
#파일인지 디렉터리인지 확인하기 (os.pathisfile, os.pathisdir)

import os
from os.path import exists,isdir,isfile

#리스트 형태로 디렉터리 불러오기
# files = os.listdir('..')

#세로로 디렉터리, 파일불러오기 불러오기
files = os.listdir()
print('files:', files)

for file in files:
    if isdir(file):
        print('<DIR>%s' %file)

for file in files:
    if isfile(file):
        print('FILE :%s' %file)
