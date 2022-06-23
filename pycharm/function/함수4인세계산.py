

# def col_rate(price, sales, per):
#     royalty = int(price*sales*per)
#     return royalty
#
# i=input('책의정가')
# price = int(i)
#
# i=input('책의 발행부수')
# sales = int(i)
#
# i=input('인세율은?')
# per = float(i)

# v=col_rate(price,sales,per)
# print('인세는', v, '원입니다.')

def col_rate(price,sales,per):
    royalty=int(price*sales*per/100)
    return royalty

i=input('책의 정가는')
price = int(i)

i=input('책의 발행부수는')
sales = int(i)

i=input('책의 인세율은')
per = float(i)
print(per)

v=col_rate(price,sales,per)
print(type(v))
print('인세는 {:,}원 입니다.' .format(v))
print('인세는 {:0,.1f}원 입니다.' .format(v))
print('인세는 {:0,.2f}원 입니다.' .format(v))








