# 인스턴스 변수
class Cat:
    # tricks = []  # 클래스 변수 뒤에 인스턴스 선언하면 인스턴스 따라간다

    def __init__(self, name):
        self.name = name
        self.tricks = []  # 인스턴스 변수 선언
        # print(self.tricks)

    def add_trick(self, trick):
        self.tricks.append(trick)  # 인스턴스 변수에 값 추가
        # print(self.tricks.append(trick))

cat1 = Cat('하늘이')
cat2 = Cat('야옹이')

cat1.add_trick('구르기')
cat2.add_trick('두발로 서기')
cat2.add_trick('죽은척 하기')

print(cat1.name, ':', cat1.tricks)
print(cat2.name, ':', cat2.tricks)
