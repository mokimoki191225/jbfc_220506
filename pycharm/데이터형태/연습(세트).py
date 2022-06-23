
#세트형

a = set('012345')
b = set('3456789')

print(a|b)
print(a&b)
print(a-b)
print(a^b)

#중복제거및정렬

a=['1','2','3','4','1','3']
print(type(a))

b=list(set(a))
print(b)
c=sorted(b)
print(c)