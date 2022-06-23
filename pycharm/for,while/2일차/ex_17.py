
#사전형 생성, 삭제, 등록

card = set(['몽호','훈주','준호'])
print(type(card))
print(card)
card.add('영목')
print(card)
card.discard('영목') #없는값 삭제시 오류난다.
card.add('영목')
print(card)
card.remove('영목')
print(card)


