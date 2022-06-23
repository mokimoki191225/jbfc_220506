
name = input('니 이름이 모니?')
print(name + '인데요? 왜요?')
order01 = input('모 묵을래?')
count = input('몇잔 묵을래?')
print('%s %s잔을 주문하셨습니다. \n잠시만 기다려주세요~^^' % (order01, count))
price = 5000
cost = price * int(count)
print('%s %s잔을 주문하셨습니다. \n결재하실 금액은 %d원입니다~^^' % (order01, count, cost))