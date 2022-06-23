
#기본
a=('1','2','3','4')

print(a[:2])
print(a[:-1])

#변경

# a[2]=9
a=list(a)
print(a)
a[2]='9'
a=tuple(a)
print(a)

#응용

data = (10,9)
a,b=data
c=a*b
print(a)
print(b)
print(c)

