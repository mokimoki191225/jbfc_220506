
#중첩리스트
#넥스디트스트럭처
card = [['훈주', '기창', '준호'], ['지연', '혜정', '현정'], ['영목', '지혁', '선화']]

print('카드1짱 \t: ', card[0])
print('카드2짱 \t: ', card[1])
print('카드3짱 \t: ', card[2])

print('카드1짱 중 1짱 \t: ', card[0][0])
print('카드2짱 중 1짱 \t: ', card[1][0])
print('카드3짱 중 1짱 \t: ', card[2][0])

print('카드1짱 중 3짱 \t: ', card[0][-1])
print('카드2짱 중 3짱 \t: ', card[1][-1])
print('카드3짱 중 3짱 \t: ', card[2][-1])

'''
#특정요소 위치구하기
reader = 훈주
dajang = card.index(reader)
print('%s는 %d 위치게 있다' %(reader,dajang))
'''
#리스트에서 특정구간에 있는 요소 추출하기
gihak = card[0:1]
na2 = card[1:]

print('기회팀은 \t:',gihak)
print('나머지는 \t:',na2)

#리스트에서 특정 위치에 요소 삽입하기(insert)
na2 = card.index('훈주')
card.insert(na2,'해진')
print('카드추가 : ', card)