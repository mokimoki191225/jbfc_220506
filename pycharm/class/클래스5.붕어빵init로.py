
#클래스생성과 객체성성

class 빵틀:
    모양=str()
    반죽=str()
    앙꼬=str()
    단가=int()

    def __init__(self,모양,반죽,앙꼬,단가):
        self.모양 = 모양
        self.반죽 = 반죽
        self.앙꼬 = 앙꼬
        self.단가 = 단가

    def 굽기(self,주문갯수):
        굽는횟수 = (주문갯수-1)/10+1
        완성시간 =  int(굽는횟수)*5
        return 완성시간

    def 가격(self,주문갯수):
        금액 = 주문갯수*self.단가
        return 금액

    def 주문(self,주문갯수,지불금액):
        대기시간 = self.굽기(주문갯수)
        주문금액 = self.가격(주문갯수)
        거스름돈 = 지불금액 - self.가격(주문갯수)
        return 대기시간, 거스름돈

#다꼬야기 주문
print('#다꼬야끼 주문 (1개 500원)')

다꼬야끼 = 빵틀('다꼬야끼','밀가루','낙지',500)

order = 20
payment = 10000

wait_time, change = 다꼬야끼.주문(order,payment)
shape             = 다꼬야끼.모양

print('{}빵 {}개를 주문하였고 {}원을 지불하였습니다.' .format(shape,order,payment))

if change==0:
    message = '손님 {}분만 기다려주세요'.format(wait_time)
elif change>0:
    message = '잔돈은 {}원 입니다. {}분만 기다려주세요'.format(change,wait_time)
elif change<0:
    message = '손님 금액이 {}원 부족합니다.'.format(change)
else:
    message = 'Error'

print('==>', end='\t')
print(message)
print('*'*50)