
# 리스트형 추가/삭제

jb_members = ['성실', '영목', '요온']
print('제이비\t:',  jb_members)

jb_members.append('혜형') #추가
print('append \t:', jb_members)

jb_members.insert(1, '승혁')
print('insert \t:', jb_members)

jb_members.remove('영목')
print('remove \t:', jb_members)

pickup = jb_members.pop(0) #인텍스 0 삭제
print('pop   \t:', jb_members, end=' ********** ') #줄 안바꾸기
print(pickup)