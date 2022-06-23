
print('##### 로토번호 생성기 #####')

a=input('발급할 로또번호 티겟 갯수를 입력하세요.[1~5] => ',);

import random

if 0 < int(a) < 0 and int(a) > 6:
    print('한번에 발급할 수 있는 티켓은 최소 1개에서 최대 5개입니다. 다시입력해주세요')
elif 0 < int(a) < 6:
    print('{}개의 로또번호 티겟을 주문하셨습니다.'.format(a))
    print('-' * 50)
    for i in range(int(a)):
        numbers = set()
        while len(numbers) < 6:
            pick_number = random.randint(1, 45)
            numbers.add(pick_number)
        print(' * 티켓{} : {}'.format(i + 1, sorted(numbers)))
    print('-' * 50)
    print('생성한 로또번호는 최종적으로 dict형으로 저장')
    # print('final_ticket = {', x ,)


