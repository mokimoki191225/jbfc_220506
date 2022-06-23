'''
#1차만 출력
dan=5
dan=int(dan)
gop=0

print(dan,'단 출 력 \n' + '-'*20)
for i in range(9):
    num=i+1
    gop=dan*num
    print(dan,'*',num,'=',gop)


#세로로 출력
for m in range(2,10) :
    print('%s\n [%d 단출력 ]' %('='*16,m))
    for n in range(1,10) :
        print('{} x {} = {}'.format(m,n,m*n))
'''

#가로로 row로 이쁘게

cols = 6
rows = int(8/cols)+1
w_space='\t\t'

for row in range(rows):
    dans=list()
    for col in range(cols):
        dan = (row*cols) + col+2
        dans.append(dan)
    for num in range(10):
        for dan in dans:
            if dan > 9:
                continue
            if num<1:
                print('{} 단 \t' .format(dan), end = w_space)
            else:
                gugutext = '{} x {} = {}'. format(dan, num, dan*num)
                print(gugutext,end=w_space)
        print()
    print()

