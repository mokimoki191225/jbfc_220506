
#디렉터리에 있는 파일목록 얻기 (os.listdir, glob.glob)

import os, glob

folder     = 'C:\Temp'
file_list1 = os.listdir(folder)
print(file_list1)

files      = 'data/*txt'
file_list2 = glob.glob(files)
print(file_list2)