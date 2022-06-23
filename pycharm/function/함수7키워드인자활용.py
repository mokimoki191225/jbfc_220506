
def introduceMycar(brand, seats=4,type='세단',price=100):
    message = '나의 차는 {b} {s}인승 {t}이다.' .format(b=brand,s=seats,t=type)
    print(message)
    message2 = '나의 차는 {s}인승이다.' .format(b=brand,s=seats,t=type)
    print(message2)
    message3 = '나의 차는 {s}인승, 가격은 {p}이다.'.format(s=seats, p=price)
    print(message3)

introduceMycar('아우디')
introduceMycar(brand='렛서스')
introduceMycar('제규어',seats=2)
introduceMycar(brand='qm',type='머슬')
introduceMycar(type='트럭',brand='qm')
introduceMycar('카니발',9,'rv')
introduceMycar('카니발',type='suv',seats=10)
introduceMycar(seats=10,brand='가',type='나') #안에서 자유롭게 정하면 된다

introduceMycar(seats=10,brand='가',type='나')


