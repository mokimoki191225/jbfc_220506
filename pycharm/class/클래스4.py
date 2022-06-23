
class MyClass:

    def __init__(self):
        print('MyClass 인스턴스 객체가 생성되어 메모리에 올라갑니다.')

    def getClassName(self):
        return 'MyClass'

    def __del__(self):
        print('MyClass 인스턴스 객체가 메모리에서 제거됩니다.')

#객체 생성
obj = MyClass()
ret=obj.getClassName()
print(ret)

for i in range(5):
    print(i)

print('모든 프로그램 종료') #__del__만 한번 더 돈다



