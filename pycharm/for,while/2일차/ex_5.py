num_data = 350
str_data = '350'

print(type(num_data))
print(type(str_data))

#에러발생
# sum = num_data + str_data
#오류 ctrl + 마우스 클릭

#데이터형변환
sum = int(str_data) + num_data
print('합계는? ', str(sum))
