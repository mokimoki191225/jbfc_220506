
#세트형 집한 연산자

test  = '아아아아아아아아?'
test2 = '아브라카다브라'
print(type(test))
print(list(test))

a = set(test)
b = set(test2)

print('집합 a=', a); print('집합 b=', b); #set 중복제거
print('합집합 a | b =', a | b)
print('교집합 a & b =', a & b)
print('여집합 a - b =', a - b)
print('차집합 a ^ b =', a ^ b)

unique_test = list(set(test))
print('중복제거 : ',unique_test)
sequance_test = sorted(set(test))
print('순서대로 : ',sequance_test)





