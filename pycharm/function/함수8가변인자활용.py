
def introduceMyFamily(my_name, *family_names,**family_info): #*는 리스트,튜플, **는 dict타입
    print('안녕하세요, 저는 %s 입니다.' %(my_name))
    print('*'*35)
    print('제 가족들의 이름은 아래와 같아요.')
    for name in family_names:
        print('*%s' %(name),end='\t')
    else:
        print()
    print('*'*35)
    for key,value in family_info.items():
        print('-%s : %s' %(key,value))

introduceMyFamily('영목','근종','점숙',
                주소='전주', 가훈='잘살자', 소망='더잘살자')


