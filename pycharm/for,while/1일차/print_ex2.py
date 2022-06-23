# 변수에 숫자담기

coffee1_name = '카페라떼';  coffee1_val = 4000;
coffee2_name = '카푸치노';  coffee2_val = 4500;
coffee3_name = '마끼야또';  coffee3_val = 5000;

# Case 1
# print('손님, ' + coffee1_name + coffee2_name + coffee3_name + '를 주문하셨습니다.')
# print('가격은 ' + coffee1_val + coffee2_val + coffee3_val + '원 입니다.')

# TypeError 발생
# 손님, 카페라떼카푸치노마끼야또를 주문하셨습니다.

print('손님, ' + coffee1_name + coffee2_name + coffee3_name + '를 주문하셨습니다.')
print('가격은 ' + str(coffee1_val + coffee2_val + coffee3_val) + '원 입니다.')

# Case 3
coffee_val = coffee1_val + coffee2_val + coffee3_val
print('손님, \n%s, %s, %s를 주문하셨습니다.' % (coffee1_name, coffee2_name, coffee3_name))
print('가격은 %d원 입니다.' % coffee_val)

# 변수에 숫자담기

coffee1_name = '바보';  coffee1_val = 10;
coffee2_name = '멍충이';  coffee2_val = 20;

print('너는' + coffee1_name + coffee2_name + '입니다.')
print('IQ는 ' + str(coffee1_val + coffee2_val) + '입니다.')

IQ=coffee1_val + coffee2_val
print('너는, \n        %s, %s 입니다.' % (coffee1_name, coffee2_name))
print('IQ는        %d 입니다.' %IQ)

name = input('니 이름이 모니?')
print(name + '인데요? 왜요?')
order = input('커피 묵을래? \n모 묵을래?')
count = input('몇잔 묵을래?')
print('%s %s잔을 주문하셨습니다. \n잠시만 기다려주세요~^^' % (order, count))
price = 5000
cost = price * int(count)
print('%s %s잔을 주문하셨습니다. \n결재하실 금액은 %d원입니다~^^' % (order, count, cost))

