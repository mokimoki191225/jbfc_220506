
card = ['준호', '지연', '종현', '지혁','준호']
print('카드사업부\t :', card)

'''#리스트에서 특정요소 위치구하기'''

reader = '준호'
dajang = card.index(reader)
print('%s는 카드사업부에서 %d번째에 위치하고 있습니다.' %(reader,dajang))

dajang = card.index(reader, 3) #3번쟤 이상부터 찾는다.
print('%s는 카드사업부에서 %d번째에 위치하고 있습니다.' %(reader,dajang))

#리스트에서 특정 위치의 요소를 변경하기

card.pop(-1)
print('카드 : ', card)

reader = '지연'
where = card.index(reader)
card [where] = '왕누나'
print('카드 :', card)

#리스트에서 특정구간에 있는 요소 추출하기
card = ['준호', '지연', '종현', '지혁','선화', '해진', '지원']
gihak = card[0:3]
na = card[3:]

print('기획팀 : ', end='');print(gihak);
print('카드팀 : ', end='');print(na);

#리스트에서 특정 위치에 요소 삽입하기(insert)
card = ['준호', '지연', '종현', '지혁','선화', '해진', '지원']
na2 = card.index('지원')
card.insert(na2,'현정')
print('카드추가 : ', card)

card = ['준호', '지연', '종현', '지혁','선화', '해진', '지원']
na2 = card.index('지원')
card.insert(na2,'혜정')
print('카드추가 : ', card)




