
#for문 예시

card = ['몽호','훈주','기창','영목','혁']
num=0

for card_m in card:
    num+=1
    print('인원%d->%s \t (이름길이%d)' %(num,card_m,len(card_m)))

print('*'*50)

size = len(card)

for idx in range(size):
    print('인원%d->%s \t (이름길이%d)' %(idx+1,card[idx],len(card[idx])))

print('*'*50)

size = len(card)
idx=0

for idx in range(size):
    idx+=1
    print('인원%d->%s \t (이름길이%d)' %(idx,card[idx],len(card[idx])))