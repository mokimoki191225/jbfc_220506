
# 정보은닉 Data Hiding 혹은 캡슐화 Encapsulation
# 클래스안의 변수를 핸들링(수정/호출)하기 위한 메소드를 선언하여 호출하는 방식

class MyFavorite:
    __hobby = '야구'
    __drink = '맥주'

    def get_hobby(self):
        return self.__hobby

    def get_drink(self):
        return self.__drink

    def set_hobby(self, hobby):
        self.__hobby = hobby

    def set_drink(self, drink):
        self.__drink = drink

myInfo = MyFavorite()
my_hobby = myInfo.get_hobby()
my_drink = myInfo.get_drink()
print('예전엔 %s를 좋아하고, %s를 즐겨마셨어요.'%(my_hobby, my_drink))

myInfo.set_hobby('골프')
myInfo.set_drink('소주')
my_hobby = myInfo.get_hobby()
my_drink = myInfo.get_drink()
print('지금은 %s를 좋아하고, %s를 즐겨마십니다.'%(my_hobby, my_drink))

myInfo.set_hobby('축구')
myInfo.set_drink('막걸리')
my_hobby = myInfo.get_hobby()
my_drink = myInfo.get_drink()
print('지금은 %s를 좋아하고, %s를 즐겨마십니다.'%(my_hobby, my_drink))

class MyCondition:
    __want1 = '집에'
    __want2 = '자고'

    def get_want1(self):
        return self.__want1

    def get_want2(self):
        return self.__want2

    def set_want1(self,want1):
        self.__want1 = want1

    def set_want2(self,want2):
        self.__want2 = want2

mywant = MyCondition()
my_want1 = mywant.get_want1()
my_want2 = mywant.get_want2()
print('지금 %s, %s 싶습니다.' %(my_want1,my_want2))

mywant.set_want1('퇴근')
mywant.set_want2('바로 하고')
my_want1 = mywant.get_want1()
my_want2 = mywant.get_want2()
print('지금 %s, %s 싶습니다.' %(my_want1,my_want2))

