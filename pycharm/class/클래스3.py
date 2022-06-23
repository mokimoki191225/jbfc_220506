
class MYClass: #객체 : 함수를 여러개 담을 수 있다.

    def __init__(self,name,a): #내장함수
        self.name = name
        self.a    = a

    def sayHello(self):
        hello = 'Hello,' + self.name+'\t 좋은날'
        print(hello)

    def sayGoodbye(self):
        hello = 'Hello,' + self.name+'\t 잘가'
        print(hello)

    def kkk(self):
        for a in range(self.a):
            a=a**2
        print(a)

myClass = MYClass('영목',100)
myClass.sayHello()
myClass.sayGoodbye()
myClass.kkk()

myClass2 = MYClass('요온',6)
myClass2.sayHello()
myClass2.sayGoodbye()
myClass.kkk()

myClass2.name='성실'
myClass2.sayHello()
myClass2.sayGoodbye()

