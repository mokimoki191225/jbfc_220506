
# r- 리더스크링 객체, 파일을 읽어올때 쓴다.
# w- 수정할때 쓴다.

# fp=open('파일경로와 파일이름','r',encodings='UTF-8')

####### 읽어오기
# fp = open("./data/text.txt","r", encoding="UTF-8")
# data = fp.read()
# print(fp.read())
# 읽어온다
# fp.close()
# 다른쪽에서 삭제도 못하고 하니까 close해준다.


####### 읽어오기
# with open("./data/text.txt","r",encoding="UTF-8") as fp:
#     data = fp.read()
# print(data)

####### 수정하기
# with open("./data/text.txt","w",encoding="UTF-8") as fp:
#     data = "데이터분석과정"
#     data+="\n 파이썬베이스드프로그래밍"
#     data+="\n 더 추가해보자"
#     fp.write(data)
#
# with open("./data/text.txt","r",encoding="UTF-8") as fp:
#     data = fp.read()
# print(data)

####### 수정하기, 파일추가하기
# with open("./data/text3.txt","w",encoding="UTF-8") as fp:
#     data = "데이터분석과정"
#     data+="\n 파이썬베이스드프로그래밍"
#     data+="\n 더 추가해보자"
#     data+="\n 추가했다잉"
#     fp.write(data)
#
# with open("./data/text2.txt","r",encoding="UTF-8") as fp:
#     data = fp.read()
# print(data)

####### 수정하기, 파일추가하기
with open("./data/text4.txt","w",encoding="UTF-8") as fp:
    data = ["김태희", "서울대', "aaa@gmail.com"]
    # data+="\n ["김태희", "서울대', "aaa@gmail.com"]
    # data+="\n ["김태희", "서울대', "aaa@gmail.com"]
    # data+="\n ["김태희", "서울대', "aaa@gmail.com"]
    fp.write(data)

with open("./data/text4.txt","r",encoding="UTF-8") as fp:
    data = fp.read()
print(data)

