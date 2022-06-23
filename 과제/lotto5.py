
num_chk_list = list('0123456789') #검증
final_ticket= dict()
import random
print(num_chk_list)

while True :
    a = input('발급할 로또번호 티겟 갯수를 입력하세요.[1~5] => ',)
    a = a.strip() #공백제거
    chk_num = True
    for char in a:
        is_num = char in num_chk_list
        chk_num=chk_num*is_num
        if not is_num:
            break
    if chk_num:
        if 0<int(a)<6:
            print('{}개의 로또번호 티겟을 주문하셨습니다.' .format(a))
            print('-' * 50)
            for i in range(int(a)) :
                numbers = set()
                while len(numbers) < 6:
                    pick_number = random.randint(1, 45)
                    numbers.add(pick_number)
                key = "티켓{}".format(i+1)
                val = sorted(numbers)
                final_ticket[key]=val
                print(" * {} : {} ".format(key, val))
            print('-' * 50)
            print('생성한 로또번호는 최종적으로 dict형으로 저장')
            print('final_ticket ={}'.format(final_ticket))
            break
        else:
            print('한번에 발급할 수 있는 티켓은 최소 1개에서 최대 5개입니다. 다시입력해주세요')
            continue
    print('한번에 발급할 수 있는 티켓은 최소 1개에서 최대 5개입니다. 다시입력해주세요')

# wrong_msg = '한번에 발급할 수 있는 티켓은 최소 1개에서 최대 5개입니다'
# wrong_msg+= '다시입력해주세요'
# print(wrong_msg)