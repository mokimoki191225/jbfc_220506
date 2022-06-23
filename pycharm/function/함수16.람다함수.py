
# def s(num):
#     return num**2
# num=2
# result=s(num)
# print(result)
# print((lambda x : x**2)(3))
# print((lambda x : x**2)(3))
# res = 5 + (lambda x : x**2)(3)
# print(res)
# fun1 = (lambda x : x**2)(3)
# print(fun1)

#제일 많이 쓸것 같다.
# fun1 = (lambda x : x**2)
# print(type(fun1))
# print(fun1(3))
#
# print((lambda x : x+10)(3))

#람다 여러개 지정
fun1 = list(map(lambda x : x**2, range(10)))
# fun2 = (lambda x : x for in range(10):)
print(fun1)

# print('환전한 금액은 {:,}원 입니다.' .format(krw))
# print('환전한 금액은 {:0,.1f}원 입니다.' .format(krw))
# print('환전한 금액은 {:0,.2f}원 입니다.' .format(krw))

a = (lambda x:x+100)(3)
print('{:,}'.format(a))

b = lambda x,y :x+y
print(b(2,2))