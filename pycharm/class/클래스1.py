
# print('환전한 금액은 {:,}원 입니다.' .format(krw))
# print('환전한 금액은 {:0,.1f}원 입니다.' .format(krw))
# print('환전한 금액은 {:0,.2f}원 입니다.' .format(krw))

var='파이썬, 클래스와 객체'
var2=[1,2,3,4,5]
var3=['1','2','3','4','5']
var4=1,2,3,4,5
var5=set(var2)

print('var \t:',var)
print('id(var) \t:',id(var))
print('type(var) \t:',type(var))

# str, str의 타입, str의 식별자 확인
print('\nstr       \t: ', str)
print('type(str) \t: ', type(str))
print('id(str)   \t: ', id(str))

# var 지역변수 __class__ 값 타입확인
print('\nvar.__class__ : ', var.__class__)
print('\nvar.__class__:', var2.__class__)
print('\nvar.__class__:', var3.__class__)
print('\nvar.__class__:', var4.__class__)
print('\nvar.__class__:', var5.__class__)

var6 = var.replace('파이썬', 'Python')
print('\nvar2    \t: ', var6)

