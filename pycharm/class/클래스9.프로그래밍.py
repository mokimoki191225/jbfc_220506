# dir() : 클래스 내부에 들어있는 객체들을 확인하는 명령문
# 이름장식  Name MangLing : __가 있는 것에 한하여 이름을 변경해 버리는 이름 장식 기법
# 변형된 규칙 : _[클래스명]__[변수명]

class MyCountry:
    __contry = 'Korea'
    city     = 'seoul'

result = dir(MyCountry) #__기본 내장변수
print(result)
