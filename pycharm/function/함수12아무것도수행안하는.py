
def my_funtion():
    pass
# my_funtion.

print(my_funtion.__doc__)

def introduce_your_family(name,*family_names,**family_info):

    '''
    위에 함수 다음으로 넣는것 지켜준다.
    가족에 대한 정보를 출력해주는 모듈
    name : 이름(str)
    family_names : 가족이름(가변형)
    family_info : 가족정보(dict형 list)
    '''