
#파일크기 구하기 (ospathgetsize)

from os.path import getsize

file1 = "./data/mydata.txt"
file2 = "./images/bpc.png"

#경로의 \는 신텍스 에러 난다. /는 맞다.

file_size1 = getsize(file1)
file_size2 = getsize(file2)

print('File Name : %s \t File Size : %d Byte' %(file1,file_size1))
print('File Name : %s \t File Size : %d Byte' %(file2,file_size2))