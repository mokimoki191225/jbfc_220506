
def exchangeUSDtoKRW(dollar):
    won=dollar*1065
    return won

usd = 2000
krw = exchangeUSDtoKRW(usd)

print('환전한 금액은 %d 원입니다.' % (krw))

# krw=exchangeUSDtoKRW()
# print('환전한 금액은 %d 원입니다.' %(krw))

def exchange(dollar):
    won=dollar*1065
    return won

usd=1000000
krw=exchange(usd)
print(type(krw))
print('환전한 금액은 {}원 입니다.' .format(krw,',d'))
print('환전한 금액은 {:,}원 입니다.' .format(krw))
print('환전한 금액은 {:0,.1f}원 입니다.' .format(krw))
print('환전한 금액은 {:0,.2f}원 입니다.' .format(krw))