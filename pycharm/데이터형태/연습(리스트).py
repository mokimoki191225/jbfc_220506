
#형태별 연습

#1. 리스트형
#1_1. 리스트호출

a=[1,2,3,4,5,6]
print(a[1])
print(a[-1])

#1_2. 리스트추가

a=[1,2,3,4,5,6]
# a.append(7)
a.insert(6,8)
print(a)

#1_3. 리스트슬라이싱
a=[1,2,3,4,5,6]
b=a[2:5]
c=a[:]
d=a[::2]
e=a[-3:]
f=a[::-1]
print(b)
print(c)
print(d)
print(e)
print(f)
#1_4. 리스트응용
a=[1,2,3,4,5,6]
#특정위치의 요소
b=3
c=a.index(b)
print(c)

#특정위치의 요소변경
a=[1,2,3,4,5,6]
a.pop(-1)
print(a)
b=2
c=a.index(b)
a[c]='two'
print(a)

#특정구간의 요소추출
a=[1,2,3,4,5,6]
b=a[0:2]
c=a[2:]
print('1',end='');print(b);
print('2',end='');print(c);

#1_5. 중첩리스트
a = [[1,2,3],[4,5,6],[7,8,9]]
print(a)
print(a[0])
print(a[0][0])
print(a[0][-1])














