
for i in range(1,10,2):
    mark='*'*i
    print(mark)

for i in range(1,10,2): #1,3,5,7,9
    mark=' '*(10-i)+'*'*i
    print(mark)

for i in range(1,10,2): # 1,3,5,7,9
    mark = '{spce} {star} {spce} i={idx}'.format(
            spce=' '*int((10-i)/2),
            star='*'*i,
            idx=i
            ) #format 함수는 {}로 해야 들어간다.
    print(mark)