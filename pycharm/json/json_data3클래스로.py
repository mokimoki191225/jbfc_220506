
class Person:
    name = str()
    age  = int()
    hometown  = str()

    def __init__(self,name,age,hometown):
        self.name = name
        self.age = age
        self.hometown = hometown

    def to_string(self):
        str = '%s의 나이는 %d살이고, 고향은 %s입니다.' %(self.name, self.age, self.hometown)
        return str

theif1 = Person("홍길동", 20 ,"율도국")
theif2 = Person("김영목", 34 ,"전주")

print(theif1.to_string())
print(theif2.to_string())