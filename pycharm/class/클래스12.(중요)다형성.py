
#오버라이딩 예제

class Developer:
    def __init__(self,name):
        self.name=name

    def coding(self):
        print('%s는 코딩을 종아합니다.'  %self.name)
        print(self.name+'is developer!!')

class PythonDeveloper(Developer):
    def coding(self):
        print('%s는 Python 코딩을 좋아합니다.' %self.name)

class JavaDeveloper(Developer):
    def coding(self):
        print('%s는 JAVA 코딩을 좋아합니다.' %self.name)

class CPPDeveloper(Developer):
    def coding(self):
        print('%s는 C++ 코딩을 좋아합니다.' %self.name)

pDeveloper = PythonDeveloper('찬영이')
jDeveloper = JavaDeveloper('준영이')
cDeveloper = CPPDeveloper('채영이')
tDeveloper = Developer('채영이') #부모만 돌려도 된다.

pDeveloper.coding()
jDeveloper.coding()
cDeveloper.coding()
tDeveloper.coding()