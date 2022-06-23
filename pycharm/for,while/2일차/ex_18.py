
# 사전형 생성

card = {'기획팀' : '준호'
        ,'기획팀' : '지연'
        ,'운영팀' : '현정'
        ,'상품팀' : '지형'}

print(type(card))
print('카드팀의수 \t :', len(card))
print(card)

#읽기
print('기획팀 \t :', card['기획팀'])
print('운영팀 \t :', card['운영팀'])

#추가
card['PA팀'] ='기창이'
print('카드추가 \t :', card)

#변경
card['기획팀'] ='종현이'
print('카드변경 \t :', card)

#삭제
del card['기획팀']
print('카드삭제 \t :', card)



